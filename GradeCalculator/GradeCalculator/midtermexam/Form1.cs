using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace GradeCalculator
{
    public partial class SplashScreen : Form
    {
        public SplashScreen()
        {
            InitializeComponent();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            GradingComputation lipat = new GradingComputation();
            progressBar1.Value += 25;
            if (progressBar1.Value >= 99)
            {
                lipat.Show();
                timer1.Enabled = false;
                this.Hide();
            }
        }
    }
}
