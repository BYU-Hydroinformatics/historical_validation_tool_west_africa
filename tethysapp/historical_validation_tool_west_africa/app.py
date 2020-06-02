from tethys_sdk.base import TethysAppBase, url_map_maker


class HistoricalValidationToolWestAfrica(TethysAppBase):
    """
    Tethys app class for Historical Validation Tool West Africa.
    """

    name = 'Historical Validation Tool West Africa'
    index = 'historical_validation_tool_west_africa:home'
    icon = 'historical_validation_tool_west_africa/images/historical_validation_tool_west_africa.jpeg'
    package = 'historical_validation_tool_west_africa'
    root_url = 'historical-validation-tool-west-africa'
    color = '#16a085'
    description = 'This app evaluates the accuracy for the historical streamflow values obtained from Streamflow Prediction Tool in West Africa.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='historical-validation-tool-west-africa',
                controller='historical_validation_tool_west_africa.controllers.home'
            ),
            UrlMap(
                name='get_discharge_data',
                url='get-discharge-data',
                controller='historical_validation_tool_west_africa.controllers.get_discharge_data'
            ),
            UrlMap(
                name='get_simulated_data',
                url='get-simulated-data',
                controller='historical_validation_tool_west_africa.controllers.get_simulated_data'
            ),
            UrlMap(
                name='get_simulated__bc_data',
                url='get-simulated-bc-data',
                controller='historical_validation_tool_west_africa.controllers.get_simulated_bc_data'
            ),
            UrlMap(
                name='get_hydrographs',
                url='get-hydrographs',
                controller='historical_validation_tool_west_africa.controllers.get_hydrographs'
            ),
            UrlMap(
                name='get_dailyAverages',
                url='get-dailyAverages',
                controller='historical_validation_tool_west_africa.controllers.get_dailyAverages'
            ),
            UrlMap(
                name='get_monthlyAverages',
                url='get-monthlyAverages',
                controller='historical_validation_tool_west_africa.controllers.get_monthlyAverages'
            ),
            UrlMap(
                name='get_scatterPlot',
                url='get-scatterPlot',
                controller='historical_validation_tool_west_africa.controllers.get_scatterPlot'
            ),
            UrlMap(
                name='get_scatterPlotLogScale',
                url='get-scatterPlotLogScale',
                controller='historical_validation_tool_west_africa.controllers.get_scatterPlotLogScale'
            ),
            UrlMap(
                name='get_volumeAnalysis',
                url='get-volumeAnalysis',
                controller='historical_validation_tool_west_africa.controllers.get_volumeAnalysis'
            ),
            UrlMap(
                name='volume_table_ajax',
                url='volume-table-ajax',
                controller='historical_validation_tool_west_africa.controllers.volume_table_ajax'
            ),
            UrlMap(
                name='make_table_ajax',
                url='make-table-ajax',
                controller='historical_validation_tool_west_africa.controllers.make_table_ajax'
            ),
            UrlMap(
                name='get-time-series',
                url='get-time-series',
                controller='historical_validation_tool_west_africa.controllers.get_time_series'),
            UrlMap(
                name='get-time-series-bc',
                url='get-time-series-bc',
                controller='historical_validation_tool_west_africa.controllers.get_time_series_bc'),
            UrlMap(
                name='get_observed_discharge_csv',
                url='get-observed-discharge-csv',
                controller='historical_validation_tool_west_africa.controllers.get_observed_discharge_csv'
            ),
            UrlMap(
                name='get_simulated_discharge_csv',
                url='get-simulated-discharge-csv',
                controller='historical_validation_tool_west_africa.controllers.get_simulated_discharge_csv'
            ),
            UrlMap(
                name='get_simulated_bc_discharge_csv',
                url='get-simulated-bc-discharge-csv',
                controller='historical_validation_tool_west_africa.controllers.get_simulated_bc_discharge_csv'
            ),
            UrlMap(
                name='get_forecast_data_csv',
                url='get-forecast-data-csv',
                controller='historical_validation_tool_west_africa.controllers.get_forecast_data_csv'
            ),
            UrlMap(
                name='get_forecast_bc_data_csv',
                url='get-forecast-bc-data-csv',
                controller='historical_validation_tool_west_africa.controllers.get_forecast_bc_data_csv'
            ),
        )

        return url_maps