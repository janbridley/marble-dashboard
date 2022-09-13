from signac_dashboard import Dashboard
from signac_dashboard.modules import StatepointList, ImageViewer, VideoViewer, TextDisplay
from signac_dashboard.modules import Notes
import signac


class PlotDashboard(Dashboard):
    def job_sorter(self, job):
        return [job.sp.phi, job.sp.kT, job.sp.replica]

    def job_title(self, job):
        pressure = 'p.f. = {}'.format(job.sp.phi)
        kT = 'kT = {}'.format(job.sp.kT)
        replica = 'rep {}'.format(job.sp.replica)
        return '; '.join((pressure, kT, replica))
    

def gsd_restart_error_msg(job):
    err = job.doc.get('restart_gsd_index_error', False)
    if err:
        return 'GSD restart error detected.'
    else:
        return ''


if __name__ == '__main__':
    modules = []
    modules.append(StatepointList())
    
    # job-level images/plots
    job_img_globs = [
        (['*.png'], 'All images', False),
        (['*-block-error.png'], 'Block error plots', False),
        (['hexatic-field.png'], 'Hexatic order field', False),
        (['*-field.png'], 'All field plots', True),
        (['local-density.png'], 'Local density distribution', True),
        (['*-full-series.png'], 'Timeseries plots', True),
        (['pressure-full-series.png'], 'Pressure timeseries', False),
        (['energy-full-series.png'], 'Energy timeseries', False),
        (['pe.png', 'pressure.png'], 'Block averaged energy and pressure', False),
    ]
    for globs, name, enabled in job_img_globs:
        modules.append(ImageViewer(img_globs=globs, name=name, enabled=enabled, context='JobContext'))
    
    # videos
    modules.append(VideoViewer(name='Animations', poster='hexatic-field.png'))
    
    # project-level images/plots
    gallery_img_globs = [
        (['gallery/pv-isotherm-kT-*.png'], 'Single-temperature PV isotherms', True),
        (['gallery/all-eos.png'], 'Full equation of state isotherms', True),
        (['gallery/local-density-distribution-kT-*-phi-*.png'], 'Local density distributions, by state point', False),
        (['gallery/local-density-distributions-kT-*.png'], 'Local density distributions, by temperature', True),
        (['gallery/local-density-distributions-phi-*.png'], 'Local density distributions, by density', False),
        (['gallery/*psi*.png', 'gallery/*hexatic*.png'], 'Hexatic order plots', False),
    ]
    for globs, name, enabled in gallery_img_globs:
        modules.append(ImageViewer(img_globs=globs, name=name, enabled=enabled, context='ProjectContext'))
        
    #modules.append(TextDisplay(name='GSD restart error?', message=gsd_restart_error_msg, enabled=False))
    config = {'PER_PAGE': 50}
    pr = signac.get_project('/gpfs/alpine/mat110/proj-shared/patchy-hexagon-equations-of-state')
    PlotDashboard(config=config, modules=modules, project=pr).main()
