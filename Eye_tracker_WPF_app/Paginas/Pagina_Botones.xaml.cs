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
    /// Lógica de interacción para Pagina_Botones.xaml
    /// </summary>
    public partial class Pagina_Botones : Page
    {
        public Pagina_Botones()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            Pagina_main pagina_main = new Pagina_main();

            this.NavigationService.Navigate(pagina_main);
        }

        private void Button_Click_Botones(object sender, RoutedEventArgs e)
        {

        }

        private void OnExecutePython(object sender, RoutedEventArgs e)
        {

        }

        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            Pagina_modificar_botones pagina_Modificar_Botones = new Pagina_modificar_botones();

            this.NavigationService.Navigate(pagina_Modificar_Botones);
        }
    }
}
