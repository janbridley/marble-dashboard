from signac_dashboard import Dashboard
from signac_dashboard.modules import StatepointList, ImageViewer, VideoViewer
from signac_dashboard.modules import Notes
import signac


class PlotDashboard(Dashboard):
    def job_sorter(self, job):
        return [job.sp.phi, job.sp.kT]

    def job_title(self, job):
        pressure = 'p.f. = {}'.format(job.sp.phi)
        kT = 'kT = {}'.format(job.sp.kT)
        replica = 'rep {}'.format(job.sp.replica)
        return '; '.join((pressure, kT, replica))


if __name__ == '__main__':
    modules = []
    modules.append(StatepointList())
    modules.append(ImageViewer(img_globs=['*.png'], name='Plots'))
    modules.append(ImageViewer(img_globs=['gallery/*.png'], name='Aggregate plots', context='ProjectContext'))
    config = {'PER_PAGE': 50}
    pr = signac.get_project('/gpfs/alpine/mat110/proj-shared/patchy-hexagon-equations-of-state')
    PlotDashboard(config=config, modules=modules, project=pr).main()
