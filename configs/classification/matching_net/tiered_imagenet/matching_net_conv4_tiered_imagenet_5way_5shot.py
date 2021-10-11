_base_ = ['matching_net_tiered_imagenet_5way_5shot_84x84_aug.py']
model = dict(
    type='MatchingNetClassifier',
    backbone=dict(type='Conv4'),
    head=dict(type='MatchingHead'))