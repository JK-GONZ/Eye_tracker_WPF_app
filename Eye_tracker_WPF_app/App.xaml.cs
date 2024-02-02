using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Linq;
using System.Threading.Tasks;
using System.Windows;
using Eye_tracker_WPF_app.Buttons;

namespace Eye_tracker_WPF_app
{
    /// <summary>
    /// Interaction logic for App.xaml
    /// </summary>
    public partial class App : Application
    {
        protected override void OnStartup(StartupEventArgs e)
        {
            // Carga la pantalla inicial
            MainWindow mainWindow = new MainWindow();
            mainWindow.Show();

            // Carga los botones desde el JSON al programa
            Botones Botones = new Botones();
            Botones.Get();

            base.OnStartup(e);
        }

        protected override void OnExit(ExitEventArgs e)
        {

            base.OnExit(e);
        }
    }
}
