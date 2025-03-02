import plotly.graph_objects as go
import plotly.io as pio
# pio.renderers.default = 'notebook'
pio.renderers.default = 'vscode'
from plotly.subplots import make_subplots
import pandas as pd

# What data to get and How to plot it
# Orders: x=ts, y='avg_px', side, quantity
    # plot as triangles, green and red, with size proportional to quantity

# Main chart: Price data
# Secondary chart: account value over time


class NTPlotter():

    @staticmethod
    def plot_account_report(df_account_report):
        # available columns:
        #    'total', 'locked', 'free', 'currency', 'account_id', 'account_type',
        #    'base_currency', 'margins', 'reported', 'info'
        for currency in df_account_report['currency'].unique():
        # print(currency)
        fig = go.Figure(data=[go.Scatter(x=df_account_report.index, y=df_account_report[df_account_report['currency'] == currency]['total'])])    
        fig.update_layout(template='plotly_dark', title=currency)
        fig.show()



    @staticmethod
    def plot_order_fills_report(df, x='ts_init'):
        # available columns:
        #    'trader_id', 'strategy_id', 'instrument_id', 'venue_order_id',
        #    'position_id', 'account_id', 'last_trade_id', 'type', 'side',
        #    'quantity', 'time_in_force', 'is_reduce_only', 'is_quote_quantity',
        #    'filled_qty', 'liquidity_side', 'avg_px', 'slippage', 'commissions',
        #    'emulation_trigger', 'status', 'contingency_type', 'order_list_id',
        #    'linked_order_ids', 'parent_order_id', 'exec_algorithm_id',
        #    'exec_algorithm_params', 'exec_spawn_id', 'tags', 'init_id', 'ts_init',
        #    'ts_last'
        # fig = go.Figure(data=[go.Scatter(x=df.index, y=df['quantity'])])
        fig = go.Figure(data=[go.Scatter(x=df['ts_init'], y=df['quantity'])])

        fig.update_layout(
            title=f'Results',
            xaxis_rangeslider_visible=False,
            template='plotly_dark'
        )

        fig.show()



    @staticmethod
        # available columns:
        #    'trader_id', 'strategy_id', 'instrument_id', 'account_id',
        #    'opening_order_id', 'closing_order_id', 'entry', 'side', 'quantity',
        #    'peak_qty', 'ts_init', 'ts_opened', 'ts_last', 'ts_closed',
        #    'duration_ns', 'avg_px_open', 'avg_px_close', 'commissions',
        #    'realized_return', 'realized_pnl'
    def plot_positions_report(df_positions_report):
        fig = go.Figure(data=[go.Scatter(x=df['ts_init'], y=df['quantity'])])

        fig.update_layout(
            title=f'Positions',
            xaxis_rangeslider_visible=False,
            template='plotly_dark'
        )

        fig.show()