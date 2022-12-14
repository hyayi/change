# model settings
norm_cfg = dict(type='SyncBN', requires_grad=True)
base_channels = 16
model = dict(
    type='IAEncoderDecoder',
    pretrained=None,
    backbone=dict(
        type='SiamUnet_diff',
        in_channels=3,
        base_channel=base_channels),
    decode_head=dict(
        type='FCNHead',
        in_channels=base_channels,
        channels=base_channels,
        in_index=-1,
        num_convs=0,
        concat_input=False,
        num_classes=2,
        loss_decode=dict(
            type='CrossEntropyLoss', use_sigmoid=False, loss_weight=1.0)),
    # model training and testing settings
    train_cfg=dict(),
    test_cfg=dict(mode='whole'))