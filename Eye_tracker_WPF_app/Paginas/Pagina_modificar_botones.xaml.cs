using System;
using System.Collections.Generic;
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

namespace Eye_tracker_WPF_app.Paginas
{
    /// <summary>
    /// Lógica de interacción para Pagina_modificar_botones.xaml
    /// </summary>
    public partial class Pagina_modificar_botones : Page
    {
        public Pagina_modificar_botones()
        {
            InitializeComponent();
        }

        private void Button_Click_Atras(object sender, RoutedEventArgs e)
        {
            Pagina_Botones pagina_botones = new Pagina_Botones();


            this.NavigationService.Navigate(pagina_botones);
        }

        private void Button_Click_Añadir(object sender, RoutedEventArgs e)
        {
            Pagina_añadir_boton pagina_Añadir_Boton = new Pagina_añadir_boton();

            this.NavigationService.Navigate(pagina_Añadir_Boton);
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {

        }

        private void Button_Click_1(object sender, RoutedEventArgs e)
        {

        }

        private void Button_Click_2(object sender, RoutedEventArgs e)
        {

        }

        private void Button_Click_3(object sender, RoutedEventArgs e)
        {

        }
    }
}
