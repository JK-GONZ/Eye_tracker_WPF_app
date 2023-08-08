using NetMQ.Sockets;
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


using System.Threading;
using NetMQ;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Collections;

namespace Eye_tracker_WPF_app.Paginas
{
    /// <summary>
    /// Lógica de interacción para Pagina_Botones.xaml
    /// </summary>
    public partial class Pagina_Botones : Page, INotifyPropertyChanged
    {
        public event PropertyChangedEventHandler? PropertyChanged;

        ObservableCollection<String> listaBotones_Contents;


        public ObservableCollection<String> ListaBotones_Contents
        {
            get { return listaBotones_Contents; }
            set { listaBotones_Contents = value; OnPropertyChanged("ListaBotones_Contents"); }
        }

        


        public Pagina_Botones(ObservableCollection<String> listaBo )
        {
            InitializeComponent();

            /*ListaBotones = new ObservableCollection<Button>
            {
                Boton1,
                Boton2,
                Boton3,
                Boton4,
                Boton5,
                Boton6,
                Boton7,
                Boton8
            };*/
            if(listaBo == null)
            {
                ListaBotones_Contents = new ObservableCollection<string>
                {
                    Boton1.Content.ToString(),
                    Boton2.Content.ToString(),
                    Boton3.Content.ToString(),
                    Boton4.Content.ToString(),
                    Boton5.Content.ToString(),
                    Boton6.Content.ToString(),
                    Boton7.Content.ToString(),
                    Boton8.Content.ToString()
                };

            } else
            {
                ListaBotones_Contents = listaBo;
            }
            

        }

        private void OnPropertyChanged(string propertyname)
        {
            if (PropertyChanged != null)
                PropertyChanged(this, new PropertyChangedEventArgs(propertyname));
        }


        private void Button_Click(object sender, RoutedEventArgs e)
        {
            Pagina_main pagina_main = new Pagina_main();

            this.NavigationService.Navigate(pagina_main);
        }


        private void Button_Click_Mod_Boton(object sender, RoutedEventArgs e)
        {
            Pagina_modificar_botones pagina_Modificar_Botones = new Pagina_modificar_botones();

            this.NavigationService.Navigate(pagina_Modificar_Botones);
        }


        private void Button_Click_Botones(object sender, RoutedEventArgs e)
        {
            if (sender is Button boton)
            {
                // Obtener el contenido (texto) del botón
                var mensaje = boton.Content.ToString();

                // Llamar a la funcion para comunicarse con Python
                var respuesta = EnviarMensajeApython(mensaje);
            }
            
        }

        public string EnviarMensajeApython(string mensaje)
        {
            using (var client = new RequestSocket())
            {
                client.Connect("tcp://localhost:5555");
                client.SendFrame(mensaje);

                // Esperar la respuesta del servidor Python
                var response = client.ReceiveFrameString();
                return response;
            }
        }
    }
}
