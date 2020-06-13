from qgis.core import (QgsProject, NULL, qgsfunction)

@qgsfunction(args='auto', group='Custom')
def qr(evento, taller, cc, feature, parent):
  if evento and taller and cc:
    import os, qrcode
    base_dir = QgsProject.instance().fileInfo().path()
    qr_dir = os.path.join(base_dir, "qr")
    filename = "{}-{}-{}".format(evento, taller, cc.replace('.',).replace("'",))
    url = "http://qgisusers.co/media/{}.pdf".format(filename)
    if not os.path.exists(qr_dir):
	    os.makedirs(qr_dir)

    filepath = os.path.join(qr_dir, "qr-{}.png".format(filename))
    qr = qrcode.QRCode(box_size=10,border=2)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(filepath)

    return filepath
  else:
    return NULL
