def hitung_luas(s):
    "menentukan luas piramida"
    
    luas =  s * s 
    print (luas)
    return luas


nama    = "Piramida"
dimensi = "3D"
rumus   = " 0.3 * s * s * t"
sisi    = "Sisi Alas Piramida : 10"
hasil   = hitung_luas(10)

htm = f"""
<!DOCTYPE html>

<html>
<head>
<title>CGIHTTPRequestHandler</title>

</head>
<body>
<h2>Bangun Geometri</h2>

<p>Nama bangun : {nama}</p>
<p>Dimensi : {dimensi}</p>
<p>Rumus luas : {rumus}</p>
<p>{sisi} cm</p>
<p>Luas : {hasil} cm</p>
<p>Terima kasih</p>
</body>
</html>"""
 
print(htm)