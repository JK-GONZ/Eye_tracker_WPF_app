using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Security;
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


namespace Eye_tracker_WPF_app.Paginas
{
    /// <summary>
    /// Lógica de interacción para Pagina_añadir_boton.xaml
    /// </summary>
    public partial class Pagina_añadir_boton : Page
    {
        public Pagina_añadir_boton()
        {
            InitializeComponent();
        }

        private void Button_Click_Atras(object sender, RoutedEventArgs e)
        {
            Pagina_modificar_botones pagina_Modificar_Botones = new Pagina_modificar_botones();

            this.NavigationService.Navigate(pagina_Modificar_Botones);
        }


        private Process _touchKeyboardProcess = null;
        private void Button_Click(object sender, RoutedEventArgs e)
        {
            string touchKeyboardPath =
                @"C:\Program Files\Common Files\Microsoft Shared\Ink\TabTip.exe";


            //replace Process.Start line from the previous listing with
            _touchKeyboardProcess = Process.Start(touchKeyboardPath);
            this.LostFocus += TouchEnabledTextBox_LostFocus;
        }

        //add this at the end of TouchEnabledTextBox's constructor

        //add this method as a member method of the class
        private void TouchEnabledTextBox_LostFocus(object sender, RoutedEventArgs eventArgs)
        {
            if (_touchKeyboardProcess != null)
            {
                _touchKeyboardProcess.Kill();
                //nullify the instance pointing to the now-invalid process
                _touchKeyboardProcess = null;
            }
        }

     }
}
