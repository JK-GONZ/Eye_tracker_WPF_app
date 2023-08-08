
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
using System.Xml.Serialization;

using System.Collections.ObjectModel;
using System.ComponentModel;

namespace Eye_tracker_WPF_app.Paginas
{

    

    public partial class Pagina_modificar_botones : Page
    {
        ObservableCollection<String> ListaBotones_Contents;

        public event PropertyChangedEventHandler? PropertyChanged;



        ObservableCollection<String> botones;


        public Pagina_modificar_botones()
        {
            InitializeComponent();


            botones = new ObservableCollection<String>();
            ListaBotones.ItemsSource = botones;


            /*
            ListaBotones_Contents = new ObservableCollection<String>();
            lista.ItemsSource = ListaBotones_Contents;*/
            
        }

        private void Button_Click_Atras(object sender, RoutedEventArgs e)
        {
            Pagina_Botones pagina_botones = new Pagina_Botones(null);


            this.NavigationService.Navigate(pagina_botones);
        }

        private void Button_Click_Eliminar(object sender, RoutedEventArgs e)
        {
            Confirmacion.Visibility = Visibility.Visible;
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            Confirmacion.Visibility = Visibility.Hidden;
        }
    }
}
