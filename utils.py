import pandas as pd


def clean_data(df: pd.DataFrame, columns: list):
    df_selected_columns = df[columns]
    df_no_nan = df_selected_columns.dropna(subset=['id_unico'])
    df_clean = df_no_nan.drop_duplicates(subset=['id_unico'])
    return df_clean


def update_df(df_new: pd.DataFrame, df_old: pd.DataFrame):
    concat_dfs = pd.concat([df_new, df_old])
    df_updated = concat_dfs.drop_duplicates(
        subset=['id_unico'],
        keep='first'
    )
    return df_updated
