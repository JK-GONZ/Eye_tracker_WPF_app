using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Eye_tracker_WPF_app.Models
{
    public class ButtonsModel
    {
        private string _id;
        private string _text;

        public string Id 
        { 
            get => _id; 
            set => _id = value; 
        }

        public string Text 
        { 
            get => _text; 
            set 
            { 
                if (_text != value)
                {
                    _text = value;
                }
            } 
        }
    }
}
