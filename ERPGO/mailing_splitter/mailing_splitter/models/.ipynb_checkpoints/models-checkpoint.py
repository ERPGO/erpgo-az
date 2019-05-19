# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, date, timedelta

class mailing_splitter(models.Model):
     _name = 'mailing_splitter.mailing_splitter'

     name = fields.Char()
     mailing_list = fields.Many2one('mail.mass_mailing', string="Mailing List")
     start_date = fields.Date(string="Start date and time")
     occurance_day = fields.Integer(string="Occurence(days)", default=1)
     email_from = fields.Char(string="Email From:", default="ERPGO team <info@erpgo.az>")
     reply_to = fields.Char(string="Reply To:", default="Jumshud Sultanov <jumshud.sultanov@erpgo.az>")

    
     @api.one
     def _populate_mailing(self):
        sample_id = self.mailing_list.id
        email_from = self.email_from
        reply_to = self.reply_to
        date = self.start_date
        kataloqs = self.env['mail.mass_mailing.list'].search([])
        for kataloq in kataloqs:
            main_list = env['mail.mass_mailing'].search([('id','=',sample_id)])
            schedule = str(date) + " 08:00:00"
            list = main_list.copy()
            list.write({'name': main_list.name, 'schedule_date': schedule, 'email_from': email_from, 'reply_to': reply_to, 'contact_list_ids': [( 4, kataloq.id)]})
            list.put_in_queue()
            date += timedelta(days=1)
        
        
sample_id = 69
email_from = 'ERPGO Blog <info@erpgo.az>'
reply_to = 'Jumshud Sultanov <jumshud.sultanov@erpgo.az>'
days_after = 1 # 1 day after scheduling will start
today = date.today()
date = today + timedelta(days=days_after)
kataloqs = env['mail.mass_mailing.list'].search([])
for kataloq in kataloqs:
    main_list = env['mail.mass_mailing'].search([('id','=',sample_id)])
    schedule = str(date) + " 08:00:00"
    list = main_list.copy()
    list.write({'name': main_list.name, 'schedule_date': schedule, 'email_from': email_from, 'reply_to': reply_to, 'contact_list_ids': [( 4, kataloq.id)]})
    list.put_in_queue()
    date += timedelta(days=1)

