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
    /// Lógica de interacción para Pagina_Juegos.xaml
    /// </summary>
    public partial class Pagina_Juegos : Page
    {
        public Pagina_Juegos()
        {
            InitializeComponent();
        }

        private void Button_Click_Botones(object sender, RoutedEventArgs e)
        {

        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            Pagina_main pagina_main = new Pagina_main();


            this.NavigationService.Navigate(pagina_main);
        }
    }
}
