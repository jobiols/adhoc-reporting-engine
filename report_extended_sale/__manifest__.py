##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Report Extended Sale Integration',
    'version': '11.0.1.2.0',
    'category': 'Reporting Subsystem',
    'sequence': 14,
    'summary': '',
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'images': [
    ],
    'depends': [
        'report_extended',
        # 'sale',
        # TODO dejamos esta dependencia hasta que movamos cierta funcionalidad
        # a un sale_document
        'l10n_ar_sale',
    ],
    'data': [
        'views/report_view.xml',
        'views/sale_order_view.xml',
        'views/sale_checkbook_views.xml',
        # 'views/company_view.xml'
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': True,
    'application': False,
}
