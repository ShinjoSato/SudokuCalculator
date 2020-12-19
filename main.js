const { app, BrowserWindow } = require('electron')
let win

function createWindow () {
  //This is for editting.
  //var subpy = require('child_process').spawn('python',['server.py']);
  //This is for .exe file. 
  var subpy = require('child_process').spawn('python',['resources/app/server.py']);

  console.log(__dirname);
  const win = new BrowserWindow({
    width: 400,
    height: 470,
    icon:'sudoku.png',
    webPreferences: { 
      enableremotemodule: true,
      nodeIntegration: true
    } 
  })

  win.loadFile('client/index.html')
  win.webContents.openDevTools()
}

app.on('ready', createWindow)

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})

app.on('activate', () => {
  if (win === null) {
    createWindow()
  }
})