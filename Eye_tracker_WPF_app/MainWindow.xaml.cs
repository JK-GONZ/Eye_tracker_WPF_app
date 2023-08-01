using Python.Runtime;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;


using Eye_tracker_WPF_app.Paginas;

namespace Eye_tracker_WPF_app
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {

        Pagina_main Pgmain = new Pagina_main ();

        public void Initialize()
        {
            string pythonDll = @"C:\\Python311\\python311.dll";
            Environment.SetEnvironmentVariable("PYTHONNET_PYDLL", pythonDll);
            PythonEngine.Initialize();
        }
        public MainWindow()
        {


            /* Handlers for window events */
            this.Closed += Windows_FinishProgram;

            Initialize();
            InitializeComponent();
            MiFrame.NavigationService.Navigate(Pgmain);
        }

        public void Windows_FinishProgram(object? sender, EventArgs e)
        {
            Application.Current.Shutdown(0);
            //Environment.Exit(0);
        }

    }
}