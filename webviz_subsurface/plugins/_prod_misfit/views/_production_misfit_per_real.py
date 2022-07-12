from datetime import datetime
from typing import Dict, List, Tuple, Union

import pandas as pd
import plotly.colors
import webviz_core_components as wcc
from dash import Input, Output, callback
from dash.development.base_component import Component
from webviz_config.webviz_plugin_subclasses import SettingsGroupABC, ViewABC
from webviz_wlf_tutorial.plugins.population_analysis.views import population

from ..._simulation_time_series.types.provider_set import ProviderSet
from .._plugin_ids import PluginIds
from ..utils import make_dataframes as makedf
from ..utils import make_figures as makefigs
from ..view_elements import Graph
from ._view_functions import _get_well_names_combined


class PlotSettings(SettingsGroupABC):
    class Ids:
        # pylint: disable=too-few-public-methods
        COLORBY = "colorby"
        SORTING_RANKING = "sorting-ranking"
        FIG_LAYOUT_HEIGHT = "fig-layout-height"

    def __init__(self) -> None:
        super().__init__("Plot Settings")

    def layout(self) -> List[Component]:
        return [
            wcc.Dropdown(
                label="Colorby",
                id=self.register_component_unique_id(PlotSettings.Ids.COLORBY),
                options=[
                    {
                        "label": "Total misfit",
                        "value": "misfit",
                    },
                    {"label": "Phases", "value": "phases"},
                    {"label": "Date", "value": "date"},
                    {"label": "None", "value": None},
                ],
                value="phases",
                multi=False,
                clearable=False,
                persistence=True,
                persistence_type="memory",
            ),
            wcc.Dropdown(
                label="Sorting/ranking",
                id=self.register_component_unique_id(PlotSettings.Ids.SORTING_RANKING),
                options=[
                    {
                        "label": "None",
                        "value": None,
                    },
                    {
                        "label": "Ascending",
                        "value": "total ascending",
                    },
                    {
                        "label": "Descending",
                        "value": "total descending",
                    },
                ],
                value="total ascending",
                multi=False,
                clearable=False,
                persistence=True,
                persistence_type="memory",
            ),
            wcc.Dropdown(
                label="Fig layout - height",
                id=self.register_component_unique_id(PlotSettings.Ids.FIG_LAYOUT_HEIGHT),
                options=[
                    {
                        "label": "Very small",
                        "value": 250,
                    },
                    {
                        "label": "Small",
                        "value": 350,
                    },
                    {
                        "label": "Medium",
                        "value": 450,
                    },
                    {
                        "label": "Large",
                        "value": 700,
                    },
                    {
                        "label": "Very large",
                        "value": 1000,
                    },
                ],
                value=450,
                clearable=False,
                persistence=True,
                persistence_type="memory",
            ),
        ]


class MisfitPerRealView(ViewABC):
    class Ids:
        # pylint: disable=too-few-public-methods
        MISFIT_GRAPH = "misfit-graph"
        PLOT_SETTINGS = "plot-settings"
    
    def __init__(self, 
        # ensemble_names: List[str],
        # dates: List[datetime],
        # phases: List[str],
        # wells: List[str],
        # all_well_collection_names: List[str],
        # realizations: List[int],
        # input_provider_set: ProviderSet,
        # ens_vectors: Dict[str, List[str]],
        # ens_realizations: Dict[str, List[int]],
        # well_collections: Dict[str, List[str]],
        # weight_reduction_factor_oil: float,
        # weight_reduction_factor_wat: float,
        # weight_reduction_factor_gas: float,
    ) -> None:
        super().__init__("Production misfit per real")

        # self.ensemble_names = ensemble_names
        # self.dates = dates
        # self.phases = phases
        # self.wells = wells
        # self.realizations = realizations
        # self.all_well_collection_names = all_well_collection_names
        # self.input_provider_set = input_provider_set
        # self.ens_vectors = ens_vectors
        # self.ens_realizations = ens_realizations
        # self.well_collections = well_collections
        # self.weight_reduction_factor_oil = weight_reduction_factor_oil
        # self.weight_reduction_factor_wat = weight_reduction_factor_wat
        # self.weight_reduction_factor_gas = weight_reduction_factor_gas


        self.add_settings_group(PlotSettings(), MisfitPerRealView.Ids.PLOT_SETTINGS)
        column = self.add_column()
        column.add_view_element(Graph(), MisfitPerRealView.Ids.MISFIT_GRAPH)

    # def set_callbacks(self) -> None:
    #     @callback(
    #         Output(self.view_element(MisfitPerRealView.Ids.MISFIT_GRAPH)
    #             .component_unique_id(Graph.Ids.GRAPH)
    #             .to_string(),
    #             "figure",),
    #         Input(),

    #     )
    #     def _update_plots(
    #         ensemble_names: List[str],
    #         selector_dates: list,
    #         selector_phases: list,
    #         selector_well_names: list,
    #         selector_well_collection_names: list,
    #         selector_well_combine_type: str,
    #         selector_realizations: List[int],
    #         colorby: str,
    #         sorting: str,
    #         figheight: int,
    #         obs_error_weight: float,
    #         misfit_exponent: float,
    #     ) -> Union[str, List[wcc.Graph]]:

    #         if not ensemble_names:
    #             return "No ensembles selected"

    #         well_names = _get_well_names_combined(
    #             self.well_collections,
    #             selector_well_collection_names,
    #             selector_well_names,
    #             selector_well_combine_type,
    #         )

    #         dframe = makedf.get_df_diff(
    #             makedf.get_df_smry(
    #                 self.input_provider_set,
    #                 ensemble_names,
    #                 self.ens_vectors,
    #                 self.ens_realizations,
    #                 selector_realizations,
    #                 well_names,
    #                 selector_phases,
    #                 selector_dates,
    #             ),
    #             obs_error_weight,
    #             self.weight_reduction_factor_oil,
    #             self.weight_reduction_factor_wat,
    #             self.weight_reduction_factor_gas,
    #             misfit_exponent,
    #         )

    #         figures = makefigs.prod_misfit_plot(
    #             dframe,
    #             selector_phases,
    #             colorby,
    #             sorting,
    #             figheight,
    #             misfit_exponent,
    #             # misfit_normalization,
    #         )

    #         return figures

        