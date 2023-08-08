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
using System.Diagnostics;

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
            string pythonDll = @"C:\Program Files\Python310\python310.dll";
            Environment.SetEnvironmentVariable("PYTHONNET_PYDLL", pythonDll);
            PythonEngine.Initialize();
        }
        public MainWindow()
        {


            /* Handlers for window events */
            this.Closed += Windows_FinishProgram;

            Initialize();
            InitializeComponent();


            //IniciarPython();



            MiFrame.NavigationService.Navigate(Pgmain);


        }

        public void Windows_FinishProgram(object? sender, EventArgs e)
        {
            Application.Current.Shutdown(0);
            //Environment.Exit(0);
        }



        public void IniciarPython()
        {
            string result = "";
            ProcessStartInfo start = new ProcessStartInfo();
            start.FileName = @"C:\Program Files\Python310\python.exe";
            // arg[0] = Path to your python script (example : "C:\\add_them.py")
            // arg[1] = first arguement taken from  C#'s main method's args variable (here i'm passing a number : 5)
            // arg[2] = second arguement taken from  C#'s main method's args variable ( here i'm passing a number : 6)
            // pass these to your Arguements property of your ProcessStartInfo instance

            start.Arguments = "Botones.py";
            start.UseShellExecute = false;
            start.WorkingDirectory = "D:\\GitHub\\Eye_tracker_WPF_app\\Eye_tracker_Python_Program\\Botones.py"; //scriptPath
            start.RedirectStandardOutput = true;
            using (Process process = Process.Start(start))
            {
                using (StreamReader reader = process.StandardOutput)
                {
                    result = reader.ReadToEnd();
                    Console.Write(result);
                }
            }
        }

    }
}