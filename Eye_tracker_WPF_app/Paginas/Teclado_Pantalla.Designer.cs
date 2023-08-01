


namespace Eye_tracker_WPF_app.Paginas
{
    partial class Teclado_Pantalla
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            MindFusion.UI.WinForms.KeyTemplate keyTemplate1 = new MindFusion.UI.WinForms.KeyTemplate();
            this.virtualKeyboard1 = new MindFusion.UI.WinForms.VirtualKeyboard();
            this.SuspendLayout();
            // 
            // virtualKeyboard1
            // 
            keyTemplate1.AlterCaseForeground = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(0)))), ((int)(((byte)(255)))));
            keyTemplate1.CornerRadius = 0;
            keyTemplate1.LowerCaseForeground = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(255)))));
            keyTemplate1.UpperCaseForeground = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(0)))), ((int)(((byte)(0)))));
            this.virtualKeyboard1.KeyTemplate = keyTemplate1;
            this.virtualKeyboard1.Location = new System.Drawing.Point(12, 12);
            this.virtualKeyboard1.Name = "virtualKeyboard1";
            this.virtualKeyboard1.Size = new System.Drawing.Size(950, 409);
            this.virtualKeyboard1.TabIndex = 0;
            this.virtualKeyboard1.TabStop = false;
            this.virtualKeyboard1.TemplateLayout = null;
            this.virtualKeyboard1.Text = "virtualKeyboard";
            this.virtualKeyboard1.Theme = MindFusion.UI.WinForms.Theme.Windows10;
            this.virtualKeyboard1.Click += new System.EventHandler(this.virtualKeyboard1_Click);
            // 
            // Teclado_Pantalla
            // 
            this.ClientSize = new System.Drawing.Size(974, 433);
            this.Controls.Add(this.virtualKeyboard1);
            this.Name = "Teclado_Pantalla";
            this.ResumeLayout(false);

        }
        #endregion

        private MindFusion.UI.WinForms.VirtualKeyboard virtualKeyboard1;
    }
}