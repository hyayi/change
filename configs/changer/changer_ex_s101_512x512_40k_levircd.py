_base_ = './changer_ex_s50_512x512_40k_levircd.py

model = dict(backbone=dict(depth=101, stem_channels=128))
load_from = '/home/lab/inseo/change/ChangerEx_s101-512x512_40k_levircd_20220710-082722.pth'
