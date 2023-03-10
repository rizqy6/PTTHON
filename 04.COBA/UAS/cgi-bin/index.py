#PROGRAM MENAMPILKAN NAMA NIM DALAM LAYANAN CGI
nama = "FAZA RIZQY SEPTIN REZSUWANDI"  
nim = "L200210015"

htm = f"""
<!DOCTYPE html>
 
<html>
<head>
<title>UAS</title>
</head>
<body>
<h1>LAYANAN WEB DENGAN CGI</h1>
<p>Saya mengakses informasi ini melalui program python.Saya mengerjakan Saya mengerjakan UAS ini secara mandiri, hasil kerja saya sendiri, terhindar dari copy paste hasil kerja orang lain</p>
<p>Nama : {nama}</p>
<p>NIM : {nim}</p>
<p>Terima kasih</p>
</body>
</html>"""
 
print(htm)