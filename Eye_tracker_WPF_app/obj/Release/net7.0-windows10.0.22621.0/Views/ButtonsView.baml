   M S B A M L   `   `   `  ���� N  JEye_tracker_WPF_app, Version=1.0.0.0, Culture=neutral, PublicKeyToken=nullE'clr-namespace:Eye_tracker_WPF_app.ViewsEye_tracker_WPF_app.Views  O,clr-namespace:Eye_tracker_WPF_app.ViewModelsEye_tracker_WPF_app.ViewModels  +    %Eye_tracker_WPF_app.Views.ButtonsView   W SPresentationCore, Version=7.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=7.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35e aSystem.Windows.Controls.Ribbon, Version=7.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089R NWindowsBase, Version=7.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35^ ZWindowsFormsIntegration, Version=7.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35H 9http://schemas.microsoft.com/winfx/2006/xaml/presentation      R NSystem.Xaml, Version=7.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     @d2http://schemas.microsoft.com/expression/blend/2008     9local'clr-namespace:Eye_tracker_WPF_app.Views     C
viewmodels,clr-namespace:Eye_tracker_WPF_app.ViewModels       � 	Resources  5  /Eye_tracker_WPF_app.ViewModels.ButtonsViewModel   buttons �� 
TargetType �� Property �� Value��%x   &	        '��        �� " ��
HeaderGrid��.���  � ��$ 40(���  � ��
 ���� ��  � ��$ 0q�.���   bg-gray#��[  � DataContext ��  �� Source# [   � ColumnDefinitions �� $��* � � RowDefinitions �� $��0.15* ��� $
��auto ��� $��* �.+�� $��0��$��0��$��Center=� �� $��0.25* ��� $��1* ��� $��0.25* � �� $
��auto �.+��� -   $��Configuración��$��0��$��0��$
��10 3q�$��60��$	��180��  
bg-warning#��[   bg-dark#��[   font-primary#��[ $��25(�$��1q��� $��0��$��1��$��Center=�$
��0 20q�$"��EYE TRACKER ACCESIBILITY APP��#��[ $��45(�$
��Bold"��� -   $��Cerrar��$��2��$��0��$
��10 3q�$��60��$	��180��  	bg-danger#��[   bg-white#��[ #��[ $��40(�$��1q��� $��0��$��1��  bg-card#��[ 
������ $��0q�$
��1270�� �� Padding$ 10q�$��0 0 0 20q�$	��Top=�$	��300��._��� 	 �� Orientation$	 
Horizontal=�.+��� $��Contenido nuevo botón: ��$��48(�#��[ �� $	��5 0q�$	��711��$��65��$��42(�$��5q�#��[ ���� *Button.Text+
 �� Mode$
 TwoWay=��� $��2��$��0��.+�� $��0 0 0 30q� �� $��1* ��� $��1* ��� $��1* �.+��� $��Agregar��$��0��$
��10 3q�$��80��$	��300��  
bg-primary#��[ #��[ #��[ $��50(�$��1q����� *
AddCommand+�� $��
Reproducir��$��1��$
��10 3q�$��80��$	��300�� 	 
bg-success#��[	 #��[ #��[ $��50(�$��0q����� *PlayCommand+�� $��Eliminar��$��2��$
��10 3q�$��80��$	��300��#��[ #��[ #��[ $��50(�$��0q����� *DeleteCommand+�� -    ��Name$ 
lstButtons��$��0q�#��[ ���� *	Buttons+ �� SelectedItem �� *SelectedItem+ �� View �� -   BotonesPanel��.P��� $��Botones�� �� Width$
 1280�� �� CellTemplate �� .R��� $��48(����� *Text+