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

using System.Diagnostics;
using Eye_tracker_WPF_app.Views;
using System.Windows.Forms;
using Eye_tracker_WPF_app.Buttons;

using System.Threading;

namespace Eye_tracker_WPF_app
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        protected Process botonesPY;
        protected Process ConfigPY = new Process();
        protected Process EyeTrackerPY;

        public void Initialize()
        {
            string pythonDll = @"C:\Program Files\Python310\python310.dll";
            Environment.SetEnvironmentVariable("PYTHONNET_PYDLL", pythonDll);
            PythonEngine.Initialize();
        }
        public MainWindow()
        {
            /* Handlers for window events */
            //this.Closed += Windows_FinishProgram;


            Initialize();
            InitializeComponent();

            IniciarPython();
            IniciarEyeTracking();


        }

        public void Windows_FinishProgram(object? sender, EventArgs e)
        {
            try
            {
                botonesPY.Kill(true);
            }
            catch (Exception exception) { System.Console.WriteLine(exception + " botones"); }
            try
            {
                EyeTrackerPY.Kill(true);
            }
            catch(Exception exception) { System.Console.WriteLine(exception + " Eyetracker"); }
            try
            {
                ConfigPY.Kill(true);
            }
            catch (Exception exception) { System.Console.WriteLine(exception + " Config"); }
            System.Windows.Application.Current.Shutdown(0);
        }

        #region Iniciar Python

        public void IniciarPython()
        {
            string rutaPython = @"C:\Program Files\Python310\python.exe";
            
            string rutaScript = System.IO.Path.GetFullPath(@"..\..\..\Resources\Botones.py");

            ProcessStartInfo startInfo = new ProcessStartInfo
            {
                FileName = rutaPython,
                Arguments = rutaScript,
                CreateNoWindow = true,
                UseShellExecute = false,
                RedirectStandardOutput = true,
                RedirectStandardError = true
            };

            botonesPY = new Process
            {
                StartInfo = startInfo 
            };

            botonesPY.Start();

            Thread.Sleep(1000);

        }
        #endregion

        #region Iniciar Eye Tracker

        public void IniciarEyeTracking()
        {
            string rutaPython = @"C:\Program Files\Python310\python.exe";

            string rutaScript = System.IO.Path.GetFullPath(@"..\..\..\Resources\EyeTracker.py");

            ProcessStartInfo startInfo = new ProcessStartInfo
            {
                FileName = rutaPython,
                Arguments = rutaScript,
                CreateNoWindow = true,
                UseShellExecute = false,
                RedirectStandardOutput = true,
                RedirectStandardError = true
            };

            EyeTrackerPY = new Process
            {
                StartInfo = startInfo
            };

            
            try
            {
                EyeTrackerPY.Start();
            }
            catch (Exception exception) { System.Console.WriteLine(exception); }
        }
        #endregion


        #region ConfigAPP
        public void ConfigAPP()
        {
            string rutaPython = @"C:\Program Files\Python310\python.exe";
            string rutaScript = System.IO.Path.GetFullPath(@"..\..\..\Resources\Ajustes.py");

            ProcessStartInfo startInfo = new ProcessStartInfo
            {
                FileName = rutaPython,
                Arguments = rutaScript,
                CreateNoWindow = true,
                UseShellExecute = false,
                RedirectStandardOutput = true,
                RedirectStandardError = true
            };

            ConfigPY = new Process
            {
                StartInfo = startInfo
            };

            ConfigPY.Start();

        }

        #endregion
    }
}