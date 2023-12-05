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
    public partial class Summary : Form
    {
        public Summary()
        {
            InitializeComponent();
        }

        private void label23_Click(object sender, EventArgs e)
        {

        }

        private void label29_Click(object sender, EventArgs e)
        {

        }

        private void label28_Click(object sender, EventArgs e)
        {

        }

        private void Summary_Load(object sender, EventArgs e)
        {
            txtname.Text = GradingComputation.nm;
            txtsn.Text = GradingComputation.sn;
            txtcourse.Text = GradingComputation.course;
            lblgp.Text = GradingComputation.gp;
            txtpg.Text = GradingComputation.pg;
            txtsw1.Text = GradingComputation.sw1;
            txtsw2.Text = GradingComputation.sw2;
            txtsw3.Text = GradingComputation.sw3;
            txtq1.Text = GradingComputation.q1;
            txtq2.Text = GradingComputation.q2;
            txtq3.Text = GradingComputation.q3;
            txtatt.Text = GradingComputation.attendance;
            txtchar.Text = GradingComputation.charr;
            lblswave.Text = GradingComputation.swave;
            asd.Text = GradingComputation.qave;
            asdasd.Text = GradingComputation.nonacad;
            lbladdpts.Text = GradingComputation.addpts;
            txteg.Text = GradingComputation.examgrade;
            txtitem.Text = GradingComputation.items;
            lblgrade2.Text = GradingComputation.tgg;
            lblgrade1.Text = GradingComputation.examgrade;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            GradingComputation lipat = new GradingComputation();
                lipat.Show();
                this.Hide();
        }
    }
}
