#!/usr/bin/python3
"""ORM to mongodb."""
import mongoengine as me

class Report(me.Document):
    """Report of heart"""

    age = me.IntField(required=True)
    gender = me.IntField(required=True)
    ap_high = me.IntField(required=True)
    ap_low = me.IntField(required=True)
    cholesterol = me.IntField(required=True)
    glucose = me.IntField(required=True)
    smoke = me.IntField(required=True)
    alcohol = me.IntField(required=True)
    activity = me.IntField(required=True)
    bmi = me.FloatField(required=True)