
# Pymaceuticals Clinical Data Analysis

## Load and Clean Data

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Mouse ID</th>
      <th>Drug</th>
      <th>Timepoint</th>
      <th>Tumor Volume (mm3)</th>
      <th>Metastatic Sites</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>q119</td>
      <td>Ketapril</td>
      <td>0</td>
      <td>45.000000</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>q119</td>
      <td>Ketapril</td>
      <td>5</td>
      <td>47.864440</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>q119</td>
      <td>Ketapril</td>
      <td>10</td>
      <td>51.236606</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>n923</td>
      <td>Ketapril</td>
      <td>0</td>
      <td>45.000000</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>n923</td>
      <td>Ketapril</td>
      <td>5</td>
      <td>45.824881</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>

    No empty values in dataframe
    The last time point is 45
    
## Tumor Response to Treatment

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Drug</th>
      <th>Capomulin (Mean)</th>
      <th>Capomulin (SEM)</th>
      <th>Infubinol (Mean)</th>
      <th>Infubinol (SEM)</th>
      <th>Ketapril (Mean)</th>
      <th>Ketapril (SEM)</th>
      <th>Placebo (Mean)</th>
      <th>Placebo (SEM)</th>
    </tr>
    <tr>
      <th>Timepoint</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>45.000000</td>
      <td>0.000000</td>
      <td>45.000000</td>
      <td>0.000000</td>
      <td>45.000000</td>
      <td>0.000000</td>
      <td>45.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>44.266086</td>
      <td>0.448593</td>
      <td>47.062001</td>
      <td>0.235102</td>
      <td>47.389175</td>
      <td>0.264819</td>
      <td>47.125589</td>
      <td>0.218091</td>
    </tr>
    <tr>
      <th>10</th>
      <td>43.084291</td>
      <td>0.702684</td>
      <td>49.403909</td>
      <td>0.282346</td>
      <td>49.582269</td>
      <td>0.357421</td>
      <td>49.423329</td>
      <td>0.402064</td>
    </tr>
    <tr>
      <th>15</th>
      <td>42.064317</td>
      <td>0.838617</td>
      <td>51.296397</td>
      <td>0.357705</td>
      <td>52.399974</td>
      <td>0.580268</td>
      <td>51.359742</td>
      <td>0.614461</td>
    </tr>
    <tr>
      <th>20</th>
      <td>40.716325</td>
      <td>0.909731</td>
      <td>53.197691</td>
      <td>0.476210</td>
      <td>54.920935</td>
      <td>0.726484</td>
      <td>54.364417</td>
      <td>0.839609</td>
    </tr>
  </tbody>
</table>
</div>

![Tumor Response to Treatment](Charts/Tumor%20Response%20to%20Treatment.png)

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Capomulin</th>
      <th>Infubinol</th>
      <th>Ketapril</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>P-Value</th>
      <td>1.996288e-16</td>
      <td>0.217114</td>
      <td>0.208587</td>
    </tr>
  </tbody>
</table>
</div>

## Metastatic Response to Treatment

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Drug</th>
      <th>Capomulin (Mean)</th>
      <th>Capomulin (SEM)</th>
      <th>Infubinol (Mean)</th>
      <th>Infubinol (SEM)</th>
      <th>Ketapril (Mean)</th>
      <th>Ketapril (SEM)</th>
      <th>Placebo (Mean)</th>
      <th>Placebo (SEM)</th>
    </tr>
    <tr>
      <th>Timepoint</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.160000</td>
      <td>0.074833</td>
      <td>0.280000</td>
      <td>0.091652</td>
      <td>0.304348</td>
      <td>0.098100</td>
      <td>0.375000</td>
      <td>0.100947</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0.320000</td>
      <td>0.125433</td>
      <td>0.666667</td>
      <td>0.159364</td>
      <td>0.590909</td>
      <td>0.142018</td>
      <td>0.833333</td>
      <td>0.115261</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0.375000</td>
      <td>0.132048</td>
      <td>0.904762</td>
      <td>0.194015</td>
      <td>0.842105</td>
      <td>0.191381</td>
      <td>1.250000</td>
      <td>0.190221</td>
    </tr>
    <tr>
      <th>20</th>
      <td>0.652174</td>
      <td>0.161621</td>
      <td>1.050000</td>
      <td>0.234801</td>
      <td>1.210526</td>
      <td>0.236680</td>
      <td>1.526316</td>
      <td>0.234064</td>
    </tr>
  </tbody>
</table>
</div>


![Metastatic Response to Treatment](Charts/Metastatic%20Response%20to%20Treatment.png)

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Capomulin</th>
      <th>Infubinol</th>
      <th>Ketapril</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>P-Value</th>
      <td>0.00002</td>
      <td>0.016157</td>
      <td>0.82785</td>
    </tr>
  </tbody>
</table>
</div>

## Survival Rates

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Drug</th>
      <th>Capomulin</th>
      <th>Infubinol</th>
      <th>Ketapril</th>
      <th>Placebo</th>
    </tr>
    <tr>
      <th>Timepoint</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>100.0</td>
      <td>100.0</td>
      <td>92.0</td>
      <td>96.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>100.0</td>
      <td>84.0</td>
      <td>88.0</td>
      <td>96.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>96.0</td>
      <td>84.0</td>
      <td>76.0</td>
      <td>80.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>92.0</td>
      <td>80.0</td>
      <td>76.0</td>
      <td>76.0</td>
    </tr>
  </tbody>
</table>
</div>

![Survival During Treatment](Charts/Survival%20During%20Treatment.png)

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Capomulin</th>
      <th>Infubinol</th>
      <th>Ketapril</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>P-Value</th>
      <td>0.010011</td>
      <td>0.903747</td>
      <td>0.738125</td>
    </tr>
  </tbody>
</table>
</div>

## Tumor Response to Treatment Summary

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Drug</th>
      <th>Capomulin</th>
      <th>Infubinol</th>
      <th>Ketapril</th>
      <th>Placebo</th>
    </tr>
    <tr>
      <th>Timepoint</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>45.000000</td>
      <td>45.000000</td>
      <td>45.000000</td>
      <td>45.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>44.266086</td>
      <td>47.062001</td>
      <td>47.389175</td>
      <td>47.125589</td>
    </tr>
    <tr>
      <th>10</th>
      <td>43.084291</td>
      <td>49.403909</td>
      <td>49.582269</td>
      <td>49.423329</td>
    </tr>
    <tr>
      <th>15</th>
      <td>42.064317</td>
      <td>51.296397</td>
      <td>52.399974</td>
      <td>51.359742</td>
    </tr>
    <tr>
      <th>20</th>
      <td>40.716325</td>
      <td>53.197691</td>
      <td>54.920935</td>
      <td>54.364417</td>
    </tr>
  </tbody>
</table>
</div>

---

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Tumor Volume Change (%)</th>
      <th>Standard Error of Mean (%)</th>
    </tr>
    <tr>
      <th>Drug</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Capomulin</th>
      <td>-19.475303</td>
      <td>3.377783</td>
    </tr>
    <tr>
      <th>Infubinol</th>
      <td>46.123472</td>
      <td>1.740427</td>
    </tr>
    <tr>
      <th>Ketapril</th>
      <td>57.028795</td>
      <td>2.056504</td>
    </tr>
    <tr>
      <th>Placebo</th>
      <td>51.297960</td>
      <td>1.985377</td>
    </tr>
  </tbody>
</table>
</div>

![Tumor Volume Change over Treatment.png](Charts/Tumor%20Volume%20Change%20over%20Treatment.png)


## Conclusions
- Looking at Tumor Response to Treatment chart and checking the result of T-test I can say that even though Infubinol and Ketapril shows slightly different dynamics than Placebo the difference is likely statistically insignificant. At the same time Capomulin shows not only signifcantly different result from the Placebo it also the only drug that proved to reduce the mean tumor volume size by the end of the test


- Ivestigating the Metastatic Response to Treatment and its T-test result I can say Ketapril shows no significant difference from Placebo while Capomulin and Infubinol influence on the slowing down of the metastasis spreading is extremely unlikely to be due chance (the former one performed a bit better). However none of the drugs was able to completely eliminate the metastatis


- Looking at the Survival Rate and its T-test results I say that Ketapril and Infubinol showed no significant difference comparing to Placebo but the Capomulin treatment boosts the chances to survive almost by the factor of 2
