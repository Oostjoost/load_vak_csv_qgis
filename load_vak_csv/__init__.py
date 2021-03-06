# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LoadVakCsv
                                 A QGIS plugin
 Vak.csv inladen in QGIS
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-03-09
        copyright            : (C) 2020 by Joost Deen/SafetyCT
        email                : j.deen@safetyct.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LoadVakCsv class from file LoadVakCsv.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Load_Vak_CSV import LoadVakCsv
    return LoadVakCsv(iface)
