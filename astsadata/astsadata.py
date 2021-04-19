import os
import pandas as pd


path = os.path.dirname(__file__)

ar1miss = pd.read_csv(f"{path}/data/ar1miss.csv", index_col=0, parse_dates=True)

arf = pd.read_csv(f"{path}/data/arf.csv", index_col=0, parse_dates=True)

beamd = pd.read_csv(f"{path}/data/beamd.csv")

birth = pd.read_csv(f"{path}/data/birth.csv", index_col=0, parse_dates=True)
birth.index = birth.index.to_period("M")

blood = pd.read_csv(f"{path}/data/blood.csv", index_col=0, parse_dates=True)

bnrf1ebv = pd.read_csv(f"{path}/data/bnrf1ebv.csv", index_col=0, parse_dates=True)

bnrf1hv = pd.read_csv(f"{path}/data/bnrf1hvs.csv", index_col=0, parse_dates=True)

cardox = pd.read_csv(f"{path}/data/cardox.csv", index_col=0, parse_dates=True)
cardox.index = cardox.index.to_period("M")

chicken = pd.read_csv(f"{path}/data/chicken.csv", index_col=0, parse_dates=True)
chicken.index = chicken.index.to_period("M")

climhyd = pd.read_csv(f"{path}/data/climhyd.csv")

cmort = pd.read_csv(f"{path}/data/cmort.csv", index_col=0, parse_dates=True)
cmort.index = cmort.index.to_period("W")

cpg = pd.read_csv(f"{path}/data/cpg.csv", index_col=0, parse_dates=True)
cpg.index = cpg.index.to_period("Y")

econ5 = pd.read_csv(f"{path}/data/econ5.csv")

EQ5 = pd.read_csv(f"{path}/data/EQ5.csv", index_col=0, parse_dates=True)

EQcount = pd.read_csv(f"{path}/data/EQcount.csv", index_col=0, parse_dates=True)
EQcount.index = EQcount.index.to_period("Y")

eqexp = pd.read_csv(f"{path}/data/eqexp.csv")

EXP6 = pd.read_csv(f"{path}/data/EXP6.csv", index_col=0, parse_dates=True)

flu = pd.read_csv(f"{path}/data/flu.csv", index_col=0, parse_dates=True)
flu.index = flu.index.to_period("M")

fmri1 = pd.read_csv(f"{path}/data/fmri1.csv", index_col=0, parse_dates=True)

gas = pd.read_csv(f"{path}/data/gas.csv", index_col=0, parse_dates=True)
gas.index = gas.index.to_period("W")

gdp = pd.read_csv(f"{path}/data/gdp.csv", index_col=0, parse_dates=True)
gdp.index = gdp.index.to_period("Q")

globtemp = pd.read_csv(f"{path}/data/globtemp.csv", index_col=0, parse_dates=True)
globtemp.index = globtemp.index.to_period("Y")

globtempl = pd.read_csv(f"{path}/data/globtempl.csv", index_col=0, parse_dates=True)
globtempl.index = globtempl.index.to_period("Y")

gnp = pd.read_csv(f"{path}/data/gnp.csv", index_col=0, parse_dates=True)
gnp.index = gnp.index.to_period("Q")

gtemp_land = pd.read_csv(f"{path}/data/gtemp_land.csv", index_col=0, parse_dates=True)
gtemp_land.index = gtemp_land.index.to_period("Y")

gtemp_ocean = pd.read_csv(f"{path}/data/gtemp_ocean.csv", index_col=0, parse_dates=True)
gtemp_ocean.index = gtemp_ocean.index.to_period("Y")

gtemp = pd.read_csv(f"{path}/data/gtemp.csv", index_col=0, parse_dates=True)
gtemp.index = gtemp.index.to_period("Y")

gtemp2 = pd.read_csv(f"{path}/data/gtemp2.csv", index_col=0, parse_dates=True)
gtemp2.index = gtemp2.index.to_period("Y")

HCT = pd.read_csv(f"{path}/data/HCT.csv", index_col=0, parse_dates=True)

hor = pd.read_csv(f"{path}/data/hor.csv", index_col=0, parse_dates=True)
hor.index = hor.index.to_period("Q")

jj = pd.read_csv(f"{path}/data/jj.csv", index_col=0, parse_dates=True)
jj.index = jj.index.to_period("Q")

lap = pd.read_csv(f"{path}/data/lap.csv", index_col=0, parse_dates=True)
lap.index = lap.index.to_period("W")

lead = pd.read_csv(f"{path}/data/lead.csv", index_col=0, parse_dates=True)

Lynx = pd.read_csv(f"{path}/data/Lynx.csv", index_col=0, parse_dates=True)
Lynx.index = Lynx.index.to_period("Y")

nyse = pd.read_csv(f"{path}/data/nyse.csv", index_col=0, parse_dates=True)

oil = pd.read_csv(f"{path}/data/oil.csv", index_col=0, parse_dates=True)
oil.index = oil.index.to_period("W")

part = pd.read_csv(f"{path}/data/part.csv", index_col=0, parse_dates=True)
part.index = part.index.to_period("W")

PLT = pd.read_csv(f"{path}/data/PLT.csv", index_col=0, parse_dates=True)

polio = pd.read_csv(f"{path}/data/polio.csv", index_col=0, parse_dates=True)
polio.index = polio.index.to_period("M")

prodn = pd.read_csv(f"{path}/data/prodn.csv", index_col=0, parse_dates=True)
prodn.index = prodn.index.to_period("M")

qinfl = pd.read_csv(f"{path}/data/qinfl.csv", index_col=0, parse_dates=True)
qinfl.index = qinfl.index.to_period("Q")

qintr = pd.read_csv(f"{path}/data/qintr.csv", index_col=0, parse_dates=True)
qintr.index = qintr.index.to_period("Q")

rec = pd.read_csv(f"{path}/data/rec.csv", index_col=0, parse_dates=True)
rec.index = rec.index.to_period("M")

sales = pd.read_csv(f"{path}/data/sales.csv", index_col=0, parse_dates=True)

salmon = pd.read_csv(f"{path}/data/salmon.csv", index_col=0, parse_dates=True)
salmon.index = salmon.index.to_period("M")

salt = pd.read_csv(f"{path}/data/salt.csv", index_col=0, parse_dates=True)

saltemp = pd.read_csv(f"{path}/data/saltemp.csv", index_col=0, parse_dates=True)

so2 = pd.read_csv(f"{path}/data/so2.csv", index_col=0, parse_dates=True)
so2.index = so2.index.to_period("W")

soi = pd.read_csv(f"{path}/data/soi.csv", index_col=0, parse_dates=True)
soi.index = soi.index.to_period("M")

soiltemp = pd.read_csv(f"{path}/data/soiltemp.csv")

speech = pd.read_csv(f"{path}/data/speech.csv", index_col=0, parse_dates=True)

star = pd.read_csv(f"{path}/data/star.csv", index_col=0, parse_dates=True)

sunspotz = pd.read_csv(f"{path}/data/sunspotz.csv", index_col=0, parse_dates=True)
sunspotz.index = sunspotz.index.to_period("Q")

tempr = pd.read_csv(f"{path}/data/tempr.csv", index_col=0, parse_dates=True)
tempr.index = tempr.index.to_period("W")

unemp = pd.read_csv(f"{path}/data/unemp.csv", index_col=0, parse_dates=True)
unemp.index = unemp.index.to_period("M")

UnempRate = pd.read_csv(f"{path}/data/UnempRate.csv", index_col=0, parse_dates=True)
UnempRate.index = UnempRate.index.to_period("M")

varve = pd.read_csv(f"{path}/data/varve.csv", index_col=0, parse_dates=True)

WBC = pd.read_csv(f"{path}/data/WBC.csv", index_col=0, parse_dates=True)
