using Eye_tracker_WPF_app.Models;
using Newtonsoft.Json;
using Newtonsoft.Json.Serialization;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;

namespace Eye_tracker_WPF_app.Buttons
{
    internal class Botones
    {
        private static string _path = Path.GetFullPath(@"..\..\..\Resources\Buttons.json");
        private string _id;
        private string _text;
        List<ButtonsModel> buttons;


        public Botones() 
        {

        }

        public List<ButtonsModel> Get()
        {
            string ButtonsFromFile;
            using (var reader = new StreamReader(_path))
            {
                ButtonsFromFile = reader.ReadToEnd();
            }
            
            
            List<ButtonsModel> buttons = DeserializeJsonFile(ButtonsFromFile);
            
            return buttons;
        }

        public static List<ButtonsModel> DeserializeJsonFile(string jsonFile)
        {
            //MessageBox.Show(jsonFile);
            List<ButtonsModel> botones = JsonConvert.DeserializeObject<List<ButtonsModel>>(jsonFile);
            
            return botones;
        }



        public void AddButton(ButtonsModel button)
        {
            List<ButtonsModel> botones = this.Get();
            try
            {
                button.Id = (int.Parse(botones.Last().Id) + 1).ToString();
            } catch (System.InvalidOperationException)
            {
                button.Id = "1";
            }
            botones.Add(button);

            var jsonToOutput = JsonConvert.SerializeObject(botones, Formatting.Indented);
            File.WriteAllText(_path, jsonToOutput);
        }


        public void RemoveButton(ButtonsModel button)
        {
            List<ButtonsModel> botones = this.Get();
            var buttonToDelete = botones.FirstOrDefault(obj => obj.Id == button.Id);

            if (buttonToDelete != null)
            {
                botones.Remove(buttonToDelete);
                var jsonToOutput = JsonConvert.SerializeObject(botones, Formatting.Indented);
                File.WriteAllText(_path, jsonToOutput);
            }
        }
    }
}
