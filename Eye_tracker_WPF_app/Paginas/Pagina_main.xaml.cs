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


using Eye_tracker_WPF_app;
using Eye_tracker_WPF_app.Paginas;
using System.Windows.Automation;
using System.Diagnostics;

namespace Eye_tracker_WPF_app.Paginas
{
    /// <summary>
    /// Lógica de interacción para Pagina_main.xaml
    /// </summary>
    /// 

    public partial class Pagina_main : Page
    {

        //MainWindow incio = new MainWindow();
        public Pagina_main()
        {
            InitializeComponent();
        }


        private void Button_Click_Botones(object sender, RoutedEventArgs e)
        {
            Pagina_Botones PgBotones = new Pagina_Botones();

            this.NavigationService.Navigate(PgBotones);
        }

        private void Button_Click_Juegos(object sender, RoutedEventArgs e)
        {

        }

        private void OnExecutePython(object sender, RoutedEventArgs e)
        {
            // Ruta al archivo Python que deseas ejecutar
            string pythonScriptPath = "D:\\GitHub\\Eye_tracker_WPF_app\\prueba.py";


            // Leer el contenido del archivo Python
            string pythonCode;
            try
            {
                pythonCode = File.ReadAllText(pythonScriptPath);
            }
            catch (FileNotFoundException)
            {
                MessageBox.Show("Archivo Python no encontrado.");
                return;
            }

            // Ejecutar el script de Python
            dynamic result;
            using (Py.GIL()) // Permite el intercambio de datos entre C# y Python
            {
                dynamic locals = new PyDict();
                dynamic globals = new PyDict();

                PythonEngine.Exec(pythonCode, globals, locals);

                result = locals.GetItem("resultado"); // "resultado" es el valor que se asigna en el script de Python
            }

            // Puedes hacer algo con el resultado si lo deseas
            // por ejemplo, mostrarlo en un MessageBox
            MessageBox.Show(result.ToString());


        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            MainWindow mainWindow = new MainWindow();
            
            mainWindow.Windows_FinishProgram(sender, EventArgs.Empty);
        }


        private void Button_Click_Calibrar1(object sender, RoutedEventArgs e)
        {
            // Ruta al archivo Python que deseas ejecutar
            string pythonScriptPath = "D:\\GitHub\\Eye_tracker_WPF_app\\Eye_tracker_Python_Program\\calibracion.py";


            // Leer el contenido del archivo Python
            string pythonCode;
            try
            {
                pythonCode = File.ReadAllText(pythonScriptPath);
            }
            catch (FileNotFoundException)
            {
                MessageBox.Show("Archivo Python no encontrado.");
                return;
            }

            // Ejecutar el script de Python
            dynamic result;
            using (Py.GIL()) // Permite el intercambio de datos entre C# y Python
            {
                dynamic locals = new PyDict();
                dynamic globals = new PyDict();

                PythonEngine.Exec(pythonCode, globals, locals);


                result = locals.GetItem("resultado"); // "resultado" es el valor que se asigna en el script de Python
            }

            // Puedes hacer algo con el resultado si lo deseas
            // por ejemplo, mostrarlo en un MessageBox
            MessageBox.Show(result.ToString());
        }

        private void Button_Click_Calibrar(object sender, RoutedEventArgs e)
        {
            string result = "";
            ProcessStartInfo start = new ProcessStartInfo();
            start.FileName = @"C:\Python311\python.exe";
            // arg[0] = Path to your python script (example : "C:\\add_them.py")
            // arg[1] = first arguement taken from  C#'s main method's args variable (here i'm passing a number : 5)
            // arg[2] = second arguement taken from  C#'s main method's args variable ( here i'm passing a number : 6)
            // pass these to your Arguements property of your ProcessStartInfo instance

            start.Arguments = "calibracion.py " + "-p shape_predictor_68_face_landmarks.dat";
            start.UseShellExecute = false;
            start.WorkingDirectory = "D:\\GitHub\\Eye_tracker_WPF_app\\Eye_tracker_Python_Program\\";//scriptPath
            start.RedirectStandardOutput = true;
            using (Process process = Process.Start(start))
            {
                using (StreamReader reader = process.StandardOutput)
                {
                    result = reader.ReadToEnd();
                    Console.Write(result);
                }
            }
            MessageBox.Show(result.ToString());
        }
    }

}
