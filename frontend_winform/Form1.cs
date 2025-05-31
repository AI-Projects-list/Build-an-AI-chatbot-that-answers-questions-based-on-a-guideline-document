using System;
using System.Net.Http;
using System.Text;
using System.Windows.Forms;
using Newtonsoft.Json.Linq;

namespace ChatBotApp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private async void btnSend_Click(object sender, EventArgs e)
        {
            using (HttpClient client = new HttpClient())
            {
                var json = $"{{\"message\": \"{txtUserInput.Text}\"}}";
                var content = new StringContent(json, Encoding.UTF8, "application/json");
                var response = await client.PostAsync("http://127.0.0.1:5000/chat", content);
                var reply = await response.Content.ReadAsStringAsync();
                dynamic result = JObject.Parse(reply);
                txtResponse.Text = result.reply;
            }
        }
    }
}