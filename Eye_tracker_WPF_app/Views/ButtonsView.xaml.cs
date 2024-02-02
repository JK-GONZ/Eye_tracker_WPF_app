using Eye_tracker_WPF_app.Buttons;
using Eye_tracker_WPF_app.ViewModels;
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

namespace Eye_tracker_WPF_app.Views
{
    /// <summary>
    /// Lógica de interacción para ButtonsView.xaml
    /// </summary>
    public partial class ButtonsView : UserControl
    {
        
        public ButtonsView()
        {
            InitializeComponent();
        }

        private void Button_Cerrar(object sender, RoutedEventArgs e)
        {
            MainWindow mainWindow= new MainWindow();
            ButtonsViewModel buttonsViewModel = new ButtonsViewModel();
            buttonsViewModel.EnviarMensajeAPython("Cerrar");
            mainWindow.Windows_FinishProgram(sender, EventArgs.Empty);
        }

        private void Button_Calibrar(object sender, RoutedEventArgs e)
        {
            MainWindow mainWindow = new MainWindow();
            mainWindow.ConfigAPP();
        }
    }
}
