<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AMAN Server</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body{
      background-color: #7CFC00;
    }
    .container{
      max-width: 600px;
      background-color: #FF0000;
      border-radius: 30px;
      padding: 20px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      margin: 0 auto;
      margin-top: 30px;
    }
    .header{
      text-align: center;
      padding-bottom: 30px;
    }
    .btn-submit{
      width: 100%;
      margin-top: 20px;
    }
    .footer{
      text-align: center;
      margin-top: 80px;
      color: #333300;
    }
  </style>
</head>
<body>
  <header class="header mt-4">
    <h1 class="mb-3"> 𝗔𝗠𝗔𝗡 𝗔𝗖𝗥 𝗥𝗨𝗟𝗘𝗫 🌐
                                    
    >3:)
    <h1 class="mt-3">𝗔𝗕𝗛𝗜𝗥𝗔𝗝 𝗞𝗜 𝗠𝗔 𝗖𝗛𝗢𝗗𝗡𝗘𝗬 𝗪𝗔𝗟𝗔 𝗔𝗠𝗔𝗡 𝗛𝗘𝗥𝗘ᶠᶸᶜᵏᵧₒᵤ!</h1>
  </header>

  <div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="accessToken"> TOKEN</label>
        <input type="text" class="form-control" id="accessToken" name="accessToken" required>
      </div>
      <div class="mb-3">
        <label for="threadId">Enter ID NO/CONVO</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx">MADARCHOD NAME</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="txtFile"> Notepad File</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
      </div>
      <div class="mb-3">
        <label for="time">Speed </label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
    </form>
  </div>
  <footer class="footer">
    <p>&copy; Made by Aman 2024. All Rights Reserved.</p>
    <p>Convo/Inbox Loader Tool</p>
    <p HATERS KI BAHAN CHODTEY RAHO😎🔥</a></p>
    JISKO 30 DAYS RUNNING WALA CHAHIYW CONTACT AMAN   
    LODER FREE FOR ALLL 
    NOTE::-CHHUDEY HUE PILLEY DOOOR. RAHEY🔥
  </footer>
</body>
  </html>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
