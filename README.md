# lc_metrics_resources

Collection of scripts to compute large scale landscape metrics.

For several examples working on the whole Amazon region we had several very similar scirpt and running configurations.

Most importanly Python packages: 'numpy', 'scipy', 'pandas', 'gdal','rasterio' and for emailing 'sendgrid' (see examplary 'conda' requirements.txt export)

In each example folder there are several scripts that make up the experiment: a shell script ('calc_lcmodel_stats_test.sh' and 'run.sh') for sending calculation to background process via e.g. the Unix/Linux 'nohup' command. Then the main python script ('second_stats_amz_prode_yearly.py' and 'stats_runner.py' scripts respectively) that imports 'lcmodel' and prepares and loads the raster into the required labelled numpy array structure. Also the metrics are selected in the main scripts. Finally, calculated metrics are collated into a 'pandas' dataframe and saved into a .csv file.
For emailsending after a long-running calculation on Google Cloud platform we used 'sendgrid', as shown in the 'demo_send_email.py' script, which would be invoked after the main Python script via the shell script. For that you need an own API key in the line 'sg = sendgrid.SendGridAPIClient("xxx")'

## Attribution for LecoS

The core module 'lcmodel.py' is based on Martin Jung's LecoS - Land cover statistics is plugin for QGIS - which uses a Connected Component to calculates landscape metrics. The use can choose to calculate single or several metrics for the raster classes.

LecoS Reference:
Martin Jung, LecoS — A python plugin for automated landscape ecology analysis, Ecological Informatics, Volume 31, January 2016, Pages 18-21, ISSN 1574-9541, http://dx.doi.org/10.1016/j.ecoinf.2015.11.006.

Licence:
This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.
