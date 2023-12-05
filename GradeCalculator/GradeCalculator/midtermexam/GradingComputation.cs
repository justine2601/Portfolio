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
    public partial class GradingComputation : Form
    {
        public GradingComputation()
        {
            InitializeComponent();
        }
        public static String nm;//
        public static String sn;//
        public static String course;//
        public static String gp;//
        public static String pg;//
        public static String sw1;//
        public static String sw2;//
        public static String sw3;//
        public static String q1;//
        public static String q2;//
        public static String q3;//
        public static String attendance;//
        public static String charr;//
        public static String swave;//
        public static String qave;//
        public static String nonacad;//
        public static String addpts;
        public static String grade;//
        public static String examgrade;//
        public static String items;//
        public static String tgg;//
        public static String ptssystem;
        private void GradingComputation_Load(object sender, EventArgs e)
        {
            lbgp.Items.Add("Prelims");
            lbgp.Items.Add("Midterms");
            lbgp.Items.Add("Finals");
            cbcourse.Items.Add("BSIT");
            cbcourse.Items.Add("BSCS");
            cbcourse.Items.Add("BSECE");
            cbcourse.Items.Add("BSID");
            cbcourse.Items.Add("BSHRM");
            cbcourse.Items.Add("BSTM");
            
        }

        private void textBox7_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox8_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox9_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {
            
        }

        private void rbgb_CheckedChanged(object sender, EventArgs e)
        {
            if (rbgb.Checked == true)
            {
                txtitems.Enabled = false;
            }
            else
            {
                txtitems.Enabled = true;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //-----------------------------------------------------------------------------
            if (lbgp.SelectedIndex == -1)
            {
                MessageBox.Show("No Inputs in Grading Period");
                return;
            }
            if (rbgb.Checked == false && rbrs.Checked == false)
            {
                MessageBox.Show("No Inputs in Exam");
                return;
            }
            if ((string.IsNullOrEmpty(txtname.Text) && (string.IsNullOrEmpty(txtsn.Text))))
            {
                MessageBox.Show("No Inputs in Name or Student Number");
                return;
            }
            if (cbcourse.SelectedIndex == -1)
            {
                MessageBox.Show("No Inputs in Course");
                return;
            }
            if ((string.IsNullOrEmpty(txtsw1.Text)&& (string.IsNullOrEmpty(txtsw2.Text))&& (string.IsNullOrEmpty(txtsw3.Text))))
            {
                MessageBox.Show("No Inputs in Seatworks");
                return;
            }
            if ((string.IsNullOrEmpty(txtq1.Text) && (string.IsNullOrEmpty(txtq2.Text)) && (string.IsNullOrEmpty(txtq3.Text))))
            {
                MessageBox.Show("No Inputs in Quizez");
                return;
            }
            if ((string.IsNullOrEmpty(txtatt.Text) && (string.IsNullOrEmpty(txtchar.Text))))
                {
                MessageBox.Show("No Inputs in Non Academic");
                return;
            }
            //-----------------------------------------------------------------------------
            double sww1, sww2, sww3, qq1, qq2, qq3, att, na;
            double swwt, seatworktotal, qqt, quiztotal;
            sww1 = double.Parse(txtsw1.Text);
            sww2 = double.Parse(txtsw2.Text);
            sww3 = double.Parse(txtsw2.Text);
            qq1 = double.Parse(txtq1.Text);
            qq2 = double.Parse(txtq2.Text);
            qq3 = double.Parse(txtq3.Text);
            att = double.Parse(txtatt.Text);
            na = double.Parse(txtchar.Text);
            swwt = sww1 + sww2 + sww3;
            seatworktotal = swwt / 3;
            qqt = qq1 + qq2 + qq3;
            quiztotal = qqt / 3;

            //TO Transfer
            string swaverage = seatworktotal.ToString();
            swave = swaverage;
            string qaverage = quiztotal.ToString();
            swave = qaverage;
            nm = txtname.Text;
            sn = txtsn.Text;
            course = cbcourse.SelectedIndex.ToString();
            if (txtpg.Enabled == false)
            {
                int x = 0;
                string pg1 = x.ToString();
                pg = pg1;
            }
            else
            {
                pg = txtpg.Text;
            }
            gp = lbgp.SelectedIndex.ToString();
            sw1 = txtsw1.Text;
            sw2 = txtsw2.Text;
            sw3 = txtsw3.Text;
            q1 = txtq1.Text;
            q2 = txtq2.Text;
            q3 = txtq3.Text;
            attendance = txtatt.Text;
            charr = txtchar.Text;
            if (txtitems.Text == null)
            {
                items = "Not Applicable";
            }
            else
            {
                items = txtitems.Text;
            }
            
            
            //endtransfer
            
            if (lbgp.SelectedItem.ToString() == "Prelims")
            {
                double totalgrade, car, atten, xy, xxyy, total, ts, x, y, stt, qtt;
                if (rbgb.Checked == true)
                {
                    ts = double.Parse(txtscore.Text);
                    total = ts * .40;
                    x = double.Parse(txtatt.Text);
                    y = double.Parse(txtchar.Text);
                    car = x / 100;
                    atten = y / 100;
                    xy = car + atten * 100;
                    xxyy = xy * .05;
                    stt = seatworktotal * .20;
                    qtt = quiztotal * .35;
                    totalgrade = total + stt + qtt + xxyy;
                    string var = xxyy.ToString();
                    nonacad = var;
                    string var2 = total.ToString();
                    examgrade = var2;
                    string var3 = totalgrade.ToString();
                    grade = var2;
                }
                else
                {
                    ts = double.Parse(txtscore.Text);
                    total = ts * .40;
                    x = double.Parse(txtatt.Text);
                    y = double.Parse(txtchar.Text);
                    car = x / 100;
                    atten = y / 100;
                    xy = car + atten * 100;
                    xxyy = xy * .05;
                    stt = seatworktotal * .20;
                    qtt = quiztotal * .35;
                    totalgrade = total + stt + qtt + xxyy;
                    string var = xxyy.ToString();
                    nonacad = var;
                    string var2 = total.ToString();
                    examgrade = var2;
                    string var3 = totalgrade.ToString();
                    grade = var2;
                }
            }
            if (lbgp.SelectedItem.ToString() == "Midterms" || lbgp.SelectedItem.ToString() == "Finals")
            {
                double totalgrade, car, atten, xy, xxyy, total, ts, x, y, stt, qtt;
                double TMG, TFG, total2;
                if (rbgb.Checked == true)
                {
                    ts = double.Parse(txtscore.Text);
                    total = ts * .40;
                    x = double.Parse(txtatt.Text);
                    y = double.Parse(txtchar.Text);
                    car = x / 100;
                    atten = y / 100;
                    xy = car + atten * 100;
                    xxyy = xy * .05;
                    stt = seatworktotal * .20;
                    qtt = quiztotal * .35;
                    totalgrade = total + stt + qtt + xxyy;
                    TMG = totalgrade / (2 / 3);
                    TFG = totalgrade / 3;
                    total2 = TMG + TFG;
                    string tg = total2.ToString();
                    //trnsfer
                    tg = tgg;
                    string var = xxyy.ToString();
                    nonacad = var;
                    string var2 = total.ToString();
                    examgrade = var2;
                    string var3 = totalgrade.ToString();
                    grade = var2;


                }
                else
                {
                    ts = double.Parse(txtscore.Text);
                    total = ts * .40;
                    x = double.Parse(txtatt.Text);
                    y = double.Parse(txtchar.Text);
                    car = x / 100;
                    atten = y / 100;
                    xy = car + atten * 100;
                    xxyy = xy * .05;
                    stt = seatworktotal * .20;
                    qtt = quiztotal * .35;
                    totalgrade = total + stt + qtt + xxyy;
                    TMG = totalgrade / (2 / 3);
                    TFG = totalgrade / 3;
                    total2 = TMG + TFG;
                    string tg = total2.ToString();
                    //trnsfer
                    tg = tgg;
                    string var = xxyy.ToString();
                    nonacad = var;
                    string var2 = total.ToString();
                    examgrade = var2;
                    string var3 = totalgrade.ToString();
                    grade = var2;
                }
            }
                Summary lipat = new Summary();
                lipat.Show();
                this.Hide();
            
        }

        private void lbgp_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (lbgp.SelectedItem.ToString() == "Prelims")
            {
                txtpg.Enabled = false;
            }
            else
            {
                txtpg.Enabled = true;
            }
        }

        private void txtpg_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
