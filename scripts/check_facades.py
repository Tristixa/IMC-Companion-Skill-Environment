"""Validate the handoff contract independently of extraction code.

Run using Python with Pillow and numpy. No game/project files are modified.
Exit 0 means automated contract checks passed, not artistic approval.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np
from PIL import Image


def expected_mask(face):
    width,height=face['px']; W=face['width_m']; H=face['wall_height_m']; G=face['gable_height_m']
    xx,rr=np.meshgrid(np.arange(width)+.5,np.arange(height)+.5)
    x=xx/width*W; y=(height-rr)/height*(H+G)
    threshold=H+G*np.power(1-np.abs(2*x/W-1),1.4)
    inside=y<=threshold
    if face.get('arch'):
        arc=face['arch']; dx=x-arc['centre_x_m']; radius=arc['half_width_m']
        circle=(dx*dx+(y-arc['straight_to_m'])**2)<=radius*radius
        opening=(np.abs(dx)<=radius)&((y<=arc['straight_to_m'])|circle)
        inside &= ~opening
    return inside

def run(SPEC, ROOT):
    checks=[]
    def check(name,ok,detail=None):checks.append({'name':name,'pass':bool(ok),'detail':detail})
    required=SPEC['faces']+SPEC.get('roof_tiles',[])+([SPEC['city_wall']] if SPEC.get('city_wall') else [])+SPEC.get('attachments',[])
    for item in required:
        path=ROOT/item['file'];check(item['file']+' exists',path.is_file())
        if not path.is_file():continue
        im=Image.open(path);check(item['file']+' exact size',list(im.size)==item['px'],list(im.size))
        a=np.array(im.convert('RGBA'));check(item['file']+' RGBA',im.mode=='RGBA')
        if item in SPEC['faces']:
            check(item['file']+' binary alpha',np.all((a[:,:,3]==0)|(a[:,:,3]==255)))
            check(item['file']+' transparent RGB scrub',np.all(a[a[:,:,3]==0,:3]==0))
        if item in SPEC['faces'] and list(im.size)==item['px']:
            mask=expected_mask(item); expected=mask.astype('uint8')*255
            check(item['file']+' analytic silhouette / all pixels',np.array_equal(a[:,:,3],expected),
                {'wrong_alpha_pixels':int(np.count_nonzero(a[:,:,3]!=expected))})
            check(item['file']+' analytic silhouette / 7px grid',np.array_equal(a[::7,::7,3],expected[::7,::7]))
            if item['type']=='wall' and not item.get('arch'):
                check(item['file']+' opaque wall rectangle',np.all(a[:,:,3]==255))
            check(item['file']+' no chroma inside silhouette',not np.any(mask&(a[:,:,0]>180)&(a[:,:,2]>180)&(a[:,:,1]<90)))
    seam_results={}
    for t in SPEC.get('roof_tiles',[])+([SPEC['city_wall']] if SPEC.get('city_wall') else []):
        path=ROOT/t['file']
        if not path.is_file():continue
        a=np.array(Image.open(path).convert('RGBA')).astype(int)
        axes=['horizontal','vertical'] if t in SPEC['roof_tiles'] else ['horizontal']
        measurements={}
        for axis in axes:
            delta=np.abs(a[:,0]-a[:,-1]) if axis=='horizontal' else np.abs(a[0]-a[-1])
            measurements[axis]={'max_channel_difference':int(delta.max()),'mean_channel_difference':round(float(delta.mean()),4)}
            check(t['file']+' '+axis+' edge continuity',delta.max()<=2,measurements[axis])
        check(t['file']+' fully opaque',np.all(a[:,:,3]==255))
        seam_results[t['file']]=measurements
    anchor_path=ROOT/'props/anchors.json';check('props/anchors.json exists when props specified',not SPEC.get('props_sheet') or anchor_path.is_file())
    names=[n.split(' (')[0] for n in SPEC.get('props_sheet',{}).get('items',[])]
    anchors=json.loads(anchor_path.read_text()) if anchor_path.is_file() else {}
    check('all named prop anchors',set(names)==set(anchors))
    residue_count=0
    for name in names:
        p=ROOT/'props'/f'{name}.png';check('props/'+name+' exists',p.is_file())
        if not p.is_file():continue
        im=Image.open(p).convert('RGBA');a=np.array(im);c=a.astype(int)
        residual=(c[:,:,0]>150)&(c[:,:,2]>150)&(c[:,:,1]<120)&(c[:,:,0]-c[:,:,1]>60)&(c[:,:,2]-c[:,:,1]>60)&(c[:,:,3]>16)
        n=int(residual.sum());residue_count+=n;check('props/'+name+' no magenta-like pixels',n==0,n)
        check('props/'+name+' transparent margin',not np.any(np.concatenate([a[0,:,3],a[-1,:,3],a[:,0,3],a[:,-1,3]])>0))
        check('props/'+name+' nonempty alpha',a[:,:,3].max()>0)
        if name in anchors:
            m=anchors[name];check('props/'+name+' metadata dimensions',m['px']==list(im.size))
            x,y=m['anchor_px'];check('props/'+name+' anchor in bounds',0<=x<im.width and 0<=y<im.height and m['height_m']>0)
    if SPEC.get('props_sheet'):
        check('prop sheet exists',(ROOT/SPEC['props_sheet']['file']).is_file())
    registration_path=ROOT/'door-registration.json'
    registrations=json.loads(registration_path.read_text()) if registration_path.is_file() else None
    for f in SPEC['faces']:
        if registrations is None or not f.get('door'):continue
        check(f['file']+' door registration exists',f['file'] in registrations)
        if f['file'] not in registrations:continue
        r=registrations[f['file']]; l,t,rr,b=r['target_leaf_bounds_px']; W,H=f['px']; total=f['wall_height_m']+f['gable_height_m']
        measured=[(l+rr)/2/W*f['width_m'],(rr-l)/W*f['width_m'],(b-t)/H*total]
        expected=[f['door'][k] for k in ['centre_x_m','width_m','height_m']]
        check(f['file']+' door landmark registration within 5cm',max(abs(a-b) for a,b in zip(measured,expected))<=.05,
            {'registered_m':measured,'note':'Verifies source landmark transform, not automatic image recognition.'})
    failures=[c for c in checks if not c['pass']]
    result={'status':'PASS' if not failures else 'FAIL','checks':len(checks),'passed':len(checks)-len(failures),
        'failed':len(failures),'required_fixed_size_images':len(required),'faces':len(SPEC['faces']),
        'props':len(names),'prop_magenta_pixels':residue_count,'seams':seam_results,'results':checks,
        'limits':['Automated checks do not approve art or verify runtime integration.',
          'Door measurements use manually inspected leaf landmarks.',
          'Prop height/depth are art estimates; perspective and ground contact require runtime review.']}
    summary=f"{result['status']}: {result['passed']}/{len(checks)} checks; {len(failures)} failures. {len(SPEC['faces'])} faces; {len(required)} exact-size images; {len(names)} props; {residue_count} magenta-like prop pixels. Roof/wall opposite-edge max difference: {max((v['max_channel_difference'] for t in seam_results.values() for v in t.values()), default=0)}/255."
    print(summary)
    for c in failures:print('FAIL:',c['name'],c['detail'])
    return 1 if failures else 0


def main():
    parser=argparse.ArgumentParser(description='Read-only facade contract check. Full-pixel silhouette comparison includes every edge pixel and a separate 7px grid. Binary alpha applies to faces; attachments/props may be antialiased. Seam tolerance: 2/255 per RGBA channel.')
    parser.add_argument('--spec',required=True,type=Path,help='Facade spec JSON.')
    parser.add_argument('--run',required=True,type=Path,help='Asset root; no files are written here. Door-registration metadata checked only when present.')
    args=parser.parse_args()
    try:
        return run(json.loads(args.spec.read_text(encoding='utf-8-sig')),args.run)
    except (OSError,ValueError,KeyError,TypeError,IndexError) as exc:
        print(f'FAIL: invalid input: {exc}')
        return 1


if __name__=='__main__':sys.exit(main())
