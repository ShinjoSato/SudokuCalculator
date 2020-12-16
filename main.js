const { app, BrowserWindow } = require('electron')
let win

function createWindow () {
  var subpy = require('child_process').spawn('python',['server.py']);

  console.log(__dirname);
  win = new BrowserWindow({
    width: 400,
    height: 490,
    icon: __dirname + '/images/megaman-green02left.png',
    webPreferences: { 
      enableremotemodule: true,
      nodeIntegration: true
    } 
  })

  win.loadFile('client/index.html')
  win.webContents.openDevTools()
  win.on('closed', () => {
    win = null
  })
}

app.on('ready', createWindow)

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  if (win === null) {
    createWindow()
  }
})