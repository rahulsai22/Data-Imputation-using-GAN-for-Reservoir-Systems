# **Data Imputation using GAN for Reservoir Systems Overview**

This project demonstrates the use of **Generative Adversarial Networks (GANs)** to perform data imputation for reservoir systems. The dataset was provided by **CDAC Pune**, and additional relevant data was obtained through direct communication with their team. The aim was to ensure realistic and constraint-aware imputation for missing values in reservoir-related datasets, outperforming traditional imputation methods such as **NSGA-II** and **NSGA-III**.

## **Key Features**

A. **Data Collaboration**:

  Collaborated with CDAC Pune to obtain detailed and structured reservoir datasets.
  Communicated with their team to gather additional relevant data for improving the imputation accuracy.

B. **Data Preprocessing**:

  Performed ETL (Extract, Transform, Load) processes to clean and prepare the dataset.
  Conducted comprehensive data analytics to understand trends, distributions, and anomalies.

C. **Feature Engineering and Selection**:

  Applied domain-specific constraints for reservoirs during feature engineering to maintain the integrity of imputed data.
  Selected features based on importance metrics to optimize model training.

D. **Generative Adversarial Networks (GANs)**:

  Leveraged GANs to generate realistic imputed values for missing data.
  Ensured that the generated values adhered to reservoir-specific constraints and patterns.

E. **Hyperparameter Tuning**:

  Experimented with various parameters (learning rate, batch size, number of epochs) to optimize GAN performance.
  Used Stratified K-Fold Validation to ensure robust model evaluation.

F. **Comparison with NSGA-II and NSGA-III**:

  Compared imputation performance with state-of-the-art methods such as NSGA-II and NSGA-III.
  Demonstrated superior performance in terms of key metrics like RMSE (Root Mean Square Error).

## **How GANs Work**

**Generative Adversarial Networks (GANs)** consist of two neural networks that compete with each other:

A. **Generator**: Generates synthetic data resembling the original data.
B. **Discriminator**: Distinguishes between real and generated data.
The generator improves by learning to create data that can fool the discriminator, while the discriminator gets better at identifying fake data. This adversarial process leads to the generation of highly realistic synthetic data.

In this project:

A. The generator created imputed values for missing data in a way that maintained the reservoir-specific constraints.
B. The discriminator ensured that these imputed values were indistinguishable from actual reservoir data.

## **Results and Metrics**

The GAN-based approach was evaluated against NSGA-II and NSGA-III. The following metrics were used for comparison:

Root Mean Square Error (RMSE): Measures the difference between observed and imputed values.

## **Comparison Results:**

A. **GAN**: Achieved an RMSE reduction of **18% **and **66%** compared to NSGA-II and NSGA-III, respectively.
B. Demonstrated superior performance across all evaluation metrics, ensuring realistic and constraint-compliant imputation.

## **Technologies Used**

A. **Programming Language**: Python  
B. **Libraries**: PyTorch, pandas, NumPy, Matplotlib  
C. **Techniques**: GANs, Feature Engineering, Hyperparameter Tuning, Stratified K-Fold Validation

## **Future Work**

A. Extend the model to work with real-time streaming reservoir data.  
B. Explore the use of Variational Autoencoders (VAEs) for comparison with GANs.  
C. Investigate the inclusion of additional domain-specific constraints for improved accuracy.

## **Acknowledgments**

Special thanks to **CDAC Pune** for providing the dataset and their collaboration in refining the project.
