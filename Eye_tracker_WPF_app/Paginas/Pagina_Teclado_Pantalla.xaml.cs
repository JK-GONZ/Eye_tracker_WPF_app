using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Forms;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

using MindFusion.UI;

namespace Eye_tracker_WPF_app.Paginas
{
    /// <summary>
    /// Lógica de interacción para Pagina_Teclado_Pantalla.xaml
    /// </summary>
    public partial class Pagina_Teclado_Pantalla : Page
    {
        public Pagina_Teclado_Pantalla()
        {
            InitializeComponent();
        }

        private void WindowsFormsHost_ChildChanged(object sender, System.Windows.Forms.Integration.ChildChangedEventArgs e)
        {
            Teclado_Pantalla keyboard = new Teclado_Pantalla();

            // Muestra el teclado en pantalla
            keyboard.Show();

            
        }
    }
    
}
