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


        private void Button_Click(object sender, RoutedEventArgs e)
        {
            Pagina_Teclado_Pantalla pagina_Teclado_Pantalla = new Pagina_Teclado_Pantalla();

            this.NavigationService.Navigate(pagina_Teclado_Pantalla);
        }

     }
}
