#!/usr/bin/env python3
# Copyright (c) 2019 The Regents of the University of Michigan
# All rights reserved.
# This software is licensed under the BSD 3-Clause License.
from signac_dashboard import Dashboard
from signac_dashboard.modules import StatepointList, ImageViewer, TextDisplay


class PlotDashboard(Dashboard):
    def job_sorter(self, job):
        return job.sp.get('coherence_time', -1)


def correlation_text(job):
    return 'Correlation coefficient: {:.5f}'.format(job.doc['correlation'])


if __name__ == '__main__':
    modules = []
    modules.append(StatepointList())
    modules.append(ImageViewer())
    modules.append(TextDisplay(name='Correlation',
                               message=correlation_text))
    PlotDashboard(modules=modules).main()
