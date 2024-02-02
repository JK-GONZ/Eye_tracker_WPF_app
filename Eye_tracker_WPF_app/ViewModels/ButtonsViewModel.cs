using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;
using Eye_tracker_WPF_app.Buttons;
using Eye_tracker_WPF_app.Commands;
using Eye_tracker_WPF_app.Models;
using Eye_tracker_WPF_app.Views;
using NetMQ;
using NetMQ.Sockets;

namespace Eye_tracker_WPF_app.ViewModels
{
    internal class ButtonsViewModel : ViewModelBase
    {
        private readonly Botones botones;
        private List<ButtonsModel> _buttons;
        private ButtonsModel _button;

        private ButtonsModel _SelectedItem;

        public ButtonsViewModel()
        {
            botones = new Botones();
            _button = new ButtonsModel();
            _buttons = botones.Get();
        }

        public ButtonsModel Button
        {
            get => _button;
            set
            {
                if (_button != value)
                {
                    _button = value;
                    OnPropertyChanged(nameof(Button));
                }
            }
        }

        public List<ButtonsModel> Buttons
        {
            get => _buttons;
            set
            {
                if (_buttons != value)
                {
                    _buttons = value;
                    OnPropertyChanged(nameof(Buttons));
                }
            }
        }

        public ButtonsModel SelectedItem
        {
            get => _SelectedItem;
            set
            {
                if(_SelectedItem != value)
                {
                    _SelectedItem = value;
                    OnPropertyChanged(nameof(SelectedItem));
                }
            }
        }


        public ICommand AddCommand
        {
            get
            {
                return new RelayCommand(AddExecute, AddCanExecute);
            }
        }

        private void AddExecute(Object button)
        {
            //Añadir Button a json
            botones.AddButton(Button);
            Buttons = botones.Get(); // Para recargar la lista de botones
        }


        private bool AddCanExecute(Object button)
        {
            return true;
        }


        public ICommand DeleteCommand
        {
            get
            {
                return new RelayCommand(DeleteExecute, DeleteCanExecute);
            }
        }

        private void DeleteExecute(Object button)
        {
            //MessageBox.Show(Button.Text);
            botones.RemoveButton(SelectedItem);
            Buttons = botones.Get(); // Para recargar la lista de botones
        }


        private bool DeleteCanExecute(Object button)
        {
            return true;
        }

        public ICommand PlayCommand
        {
            get
            {
                return new RelayCommand(PlayExecute, PlayCanExecute);
            }
        }

        private void PlayExecute(Object button)
        {
            using (var client = new RequestSocket())
            {
                client.Connect("tcp://localhost:5555");
                client.SendFrame(SelectedItem.Text);

                // Esperar la respuesta del servidor Python
                var response = client.ReceiveFrameString();
                //MessageBox.Show(response);
            }
        }

        private bool PlayCanExecute(Object button)
        {
            return true;
        }


        public void EnviarMensajeAPython(string mensaje)
        {
            using (var client = new RequestSocket())
            {
                client.Connect("tcp://localhost:5555");
                client.SendFrame(mensaje);

                // Esperar la respuesta del servidor Python
                var response = client.ReceiveFrameString();
            }
        }
    }
}
