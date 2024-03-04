import pandas as pd


def get_icd_dict(table):
    data = pd.DataFrame(table)
    table_dict = data.loc[:,['id', 'name']].set_index('id').to_dict()['name']

    return table_dict


def get_specialty_dict(table):
    data = pd.DataFrame(table)
    table_dict = data.loc[:, ['id', 'name']].set_index('id').to_dict()['name']

    return table_dict


class CorporateCalculations:
    def __init__(self, dataframe):
        self.corp_table = dataframe

    def claims_by_period(self):
        group_data = self.corp_table.groupby('period', as_index=False).agg(CLAIMS=('claim_id', 'count')).sort_values('period')
        return group_data

    def claims_volume_ytd(self):
        group_data = self.corp_table.groupby('period', as_index=False).agg(CLAIMS=('claim_id', 'count')).sort_values('period')
        group_data['YTD_CUM'] = group_data['CLAIMS'].cumsum()
        group_data['MO_AVE'] = (group_data['YTD_CUM'] / (group_data['period']).astype(float)).astype(int)

        return group_data

    def claims_volume_period(self):
        group_data = self.corp_table.groupby('trans_date', as_index=False).agg(CLAIMS_DAILY=('claim_id', 'count'))

        return group_data

    def claims_member_period(self):
        group_data = self.corp_table.pivot_table(index='mem_acct', columns='period', values='claim_id', aggfunc='count')

        return group_data

    def charges_member_period(self):
        group_data = self.corp_table.pivot_table(index='mem_acct', columns='period', values='charge_allowed', aggfunc='sum')

        return group_data

    def claims_member_quarter(self):
        group_data = self.corp_table.pivot_table(values='claim_id', index='mem_acct', aggfunc='count', columns='quarter').reset_index()

        return group_data

    def claims_charges_ytd(self):
        group_data = (self.corp_table.groupby('period', as_index=False)
                      .agg(CHARGES=('charge_allowed', 'sum'), CHARGE_AVE=('charge_allowed', 'mean'))
                      .sort_values('period'))
        group_data['YTD_CUM'] = group_data['CHARGES'].cumsum()
        group_data['3_MONTH_AVE'] = round(group_data['CHARGES'].rolling(3).mean().fillna(0)).astype(int)

        return group_data

    def claims_charges_period(self):
        group_data = self.corp_table.groupby('trans_date', as_index=False).agg(CLAIM_CHARGE_AVE=('charge_allowed', 'mean'))

        return group_data


class CorporateTables:
    def __init__(self, dataframe):
        self.corp_table = dataframe

    def get_quarter_charges(self):
        table = self.corp_table.groupby('quarter', as_index=False)['charge_allowed'].sum()

        return table

    def get_icd_table(self):
        icd_table = self.corp_table()

        return icd_table


class AnalyticTables:
    def __init__(self, dataframe):
        self.analytic_table = dataframe

    def get_charges(self, axis_col):
        table = self.analytic_table.groupby(axis_col, as_index=False)['charge_allowed'].sum()

        return table

    def get_claims(self, axis_col):
        table = self.analytic_table.groupby(axis_col, as_index=False)['charge_allowed'].count()

        return table

    def get_charge_ave(self, axis_col):
        table = self.analytic_table.groupby(axis_col, as_index=False)['charge_allowed'].mean()

        return table

    def get_member_count(self, axis_col):
        table = self.analytic_table.groupby(axis_col, as_index=False)['mem_acct_id'].nunique()

        return table

    def get_dist_member_claims(self):
        table = self.analytic_table.pivot_table(values='claim_id', index='mem_acct_id', aggfunc='count',
                                                columns='quarter')
        return table

    def get_heat_category_table(self, category):
        table = self.analytic_table.pivot_table(index='period', columns=category, values='charge_allowed',
                                                aggfunc='count', fill_value=0)

        return table

    def get_icd_spec_pivot(self):
        table = self.analytic_table.loc[:,['injury_disease_id', 'specialty_id', 'charge_allowed']]
        group_icd = table.groupby('injury_disease_id', as_index=False)['charge_allowed'].count().nlargest(10,
                                                                                                       'charge_allowed')
        icd_list = group_icd['injury_disease_id'].to_list()
        table = table[table['injury_disease_id'].isin(icd_list)]
        group_spec = table.groupby('specialty_id', as_index=False)['charge_allowed'].count().nlargest(10,
                                                                                                    'charge_allowed')
        spec_list = group_spec['specialty_id'].to_list()
        table = table[table['specialty_id'].isin(spec_list)]
        table = table.pivot_table(index='injury_disease_id', columns='specialty_id', values='charge_allowed',
                                aggfunc='count', fill_value=0)

        return table
