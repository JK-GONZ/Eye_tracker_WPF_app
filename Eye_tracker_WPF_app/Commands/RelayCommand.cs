using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;

namespace Eye_tracker_WPF_app.Commands
{
    internal class RelayCommand : ICommand
    {
        //  Delegados
        private readonly Action<object> _execute; //Devuelve void
        private readonly Predicate<object> _canExecute; //Devuelve bool

        public RelayCommand(Action<object> execute, Predicate<object> canExecute)
        {
            _execute = execute;
            _canExecute = canExecute;
        }

        public RelayCommand(Action<object> execute) : this(execute, null)
        {

        }
        public bool CanExecute(object? parameter)
        {
            return _canExecute == null ? true: _canExecute(parameter);
        }

        public void Execute(object? parameter)
        {
            _execute(parameter);
        }


        public event EventHandler? CanExecuteChanged
        {
            add
            {
                CommandManager.RequerySuggested += value;
            }
            remove
            {
                CommandManager.RequerySuggested -= value;
            }
        }

        
    }
}
