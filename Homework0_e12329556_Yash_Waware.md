#### Homework0_e12329556_Yash_Waware

# HeatMech | Drilling Hole
## Problem Description
 <script type="text/javascript" async
    src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
  </script>
<math xmlns="http://www.w3.org/1998/Math/MathML"></math>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
</script>
Investigate the part under different drilling conditions. The problem is depicted below:

<p align="center">
  <img src="image1.png" alt="Problem Description" width="40%">
</p>

The geometry of the model is the quadratic part given below:
<P align="center">
  <img src="part_reworked.png" alt="Geometry of the model" width="40%">
</p>

The whole part is made of steel (S235JR). A through bore is drilled in the middle of the part. Due to drilling, heat power $P$ is transferred into the part through the surface of the hole ($S_{hole}$). It is assumed that the heat power homogeneously contributes over the hole surface. During the drilling, the part is clamped on two opposite sides ($S_{fixed}$). The clamping must be modelled using zero displacement boundary conditions (fixed). The fixation is initially stress-free at ambient air temperature $T_r$. The part gets cooled by water, with the temperature $T_w$. The water runs over the top and unclamped side surfaces ($S_{cooled}$). On the bottom ($S_{air}$), it's surrounded by an airstream with an ambient temperature of $T_r$. Additionally, we neglect all heat transfer through the clamped sides and assume that the drilling speed is low compared to the heat propagation.

Create an appropriate FE model and investigate the following questions:

* What is the maximal temperature under normal operation?
* What is the maximal temperature if the water cooling fails?
* What are the maximum occurring thermal deformations in the above two cases?
* Could temperature-induced stresses pose a problem?

Use the given values:

|Variable|Value|
|--|:--:|
|drill hole radius $R$ in mm|5|
|Height $H$ in mm|30|
|Lenght $L$ in mm|100|
|Produced heat power in W|200|
|Heat transfer coefficient steel-air $\alpha_{air}$ in W/(m$^2$·K)|20|
|Heat transfer coefficient steel-water $\alpha_{water}$ in W/(m$^2$·K)|600|
|Density of S235JR $\rho$ in kg/m³|7850|
|E-modulus of S235JR in N/m²|2.00E+11|
|Thermal expansion of S235JR in 1/K |12E-6|
|Poisson number of S235JR |0.29|
|Heat capacity of S235JR in J/K|461|
|Heat conductivity of S235JR in W/mK |50|
|Ambient temperatue of air $T_r$ in °C|20|
|Temperature of water $T_w$ in °C |20|

To complete the homework assignment, follow the tasks and questions below.

## Assignment

### 1. Create a suitable mesh for the problem **(4 Points)**
* Create a hexahedral mesh.
* Define the necessary regions and assign meaningful names.
* Create the .cdb file in cubit and convert it to .cfs fromat by ‘cfs -g geometry‘ command (geometry.xml file is provided with the assignment). **(2.0 Points)** 
* Load the converted file in Paraview and create an image showing the mesh size and the different regions. **(1.5 Points)**

<p align="center">
  <img src="Region_Image.png" alt="Image Showing mesh size and different region" width="60%">
</p>

* How many nodes and elements does your mesh have? **(0.5 Points)**

Answer: 78811 nodes and 22546 elements

### 2. Modelling Assumptions **(6 Points)**

2.1. What are the modelling assumptions in the thermal model? Consider the material, analysis type, pde, etc. State at least 4 assumptions and justify them briefly. (**3.0 Points**)

Answer:  The modelling assumptions in thermal model are as follows;
    
    1. Isotropic Material: Material property such as heat conductivity is isotropic same in all directions. 
    2. Material Homogeneous: Thermal properties are constant throughout the volume.
    3. Steady-state: The system is in thermal equilibrium such that there is no significant change in the temperature with respect to time.
    4. Internal heat generation: It is assumed there is no internal heat generation within the material. The assumption help simplyfy the governing PDE.
    5. Stress-free: It is assumed that initially the body is stress-free at ambient air temperature.


2.2. What are the modelling assumptions in the mechanical model and for the coupling? Consider the material, analysis type, pde, etc. State at least 4 assumptions and justify them briefly. (**3.0 Points**)

Answer: The modelling assumptions in the mechanical model and for the coupling are as follows;

    1. Linear Elasticity: The material is considered to have linear elastic properties, which indicate that the deformation is directly proportional to the applied stress.
    2. Material Isotropic: It is assumed that the material is isotropic, which means that the direction of loading has no effect on its properties.
    3. Steady-State: It is assumed that the analysis is in a steady-state situation, which means that neither the temperature nor the deformation vary over time.
    4. Thermal Conductivity: It is assumed that the material has a constant thermal conductivity. we assume that materials that have the same thermal conductivity throughout.
    5. The structure is free of internal stress in the given initial configuration at a room temperature of 293K i.e. (dof="x", "y", "z" value="0") and clamping for zero displacement (comp dof="x", "y", "z").
    

### 3. Drilling at normal operation **(11 Points)**


3.1. Setup an appropriate simulation input for CFS. You need to:

  - define the domain and assign a material,
  - specify an appropriate PDE and analysis type,
  - define the required boundary conditions,
  - specify postprocessing results.

Describe briefly chosen PDEs, analysis types, BCs and coupiling. (**2.0 Points**)

Answer: Heat Conduction PDE helps to understand and predict the temperature distribution within a material. 

$$ {\rho c_{\textrm{m}} \frac{\partial T}{\partial t} -\nabla \cdot ({k\nabla{T}}) = \dot{{q}}} $$

where ρ is the mass density, $c_{\textrm{m}}$ the specific heat capacity (per unit mass), k the thermal
conductivity and q the heat flux density.

In this study we try to understand the heat transfer in drilling process by prescribing heatflux density, bulk temperature and heat transfer coefficient. Heat transport defines the surface through which heat is transfered between two media namely steel-air and steel-water. A steady state static analysis is considered and results are stored as temperature and heat flux. As boundary conditions heat flux and heat transport quantities are visualized. The top surface along with 2 side surfaces which are normal to the y direction are water cooled. Bottom surface remains air-cooled during the drilling operation. The fixed surfaces which are normal to the x direction have 0 heat flux. 


3.2. Give the unit of the prescribed heat flux density $\dot{q}_s$ **(0.5 Points)**

Answer: Heat flux density $\dot{q}_s$ = P/(2*$\pi$*r*h) [W/m^2]


3.3. Compute the heat flux density, which has to be prescribed at the source surface **(0.5 Points)**

Answer: Heat flux density  $\dot{q}_s$ = P/(2*$\pi$*r*h) = 212206.6 [W/m^2]


3.4. Visualize the temperature distribution in paraview (with only 10 colors in the palette) **(1.0 Point)**

<p align="center">
  <img src="temperature_distribution.png" alt="Temperature distribution for bottom surface" width="60%">
</p>

<p align="center">
  <img src="temperature_distribution2.png" alt="Temperature distribution for top surface" width="60%">
</p>

The first image shows the bottom surface which has highest temperature since air transports less heat as compared to the water which can be seen in second image.


3.5. Visualize the vector field of the heat flux density with a glyph-plot in the z-x plane (y=0) (**1.5 Points**)

<p align="center">
  <img src="Heatflux.png" alt="Heat flux density in z-x plane" width="60%">
</p>


3.6. Why is an output of heat flux density defined on elements and not at nodes? Can we compute a heat flux at a node on the reference element? **(1.5 Points)**

Answer: We integrate the over a surface area to get the results
$${\mathbf q} = - k \cdot \nabla T$$
FEA uses interpolation functions (shape functions) to approximate the variation of field variables within elements. Heat flux density, being a rate of flow, is more naturally represented using these interpolation functions over the volume of an element rather than just at discrete nodes. Heat flux density is a continuous field variable, and nodal values represent only the values at specific locations, and interpolating these nodal values across the element may not capture the variations as accurately as using element-wise interpolation functions.

Inorder to compute heat flux at a node, we need to use the temperature gradient at that perticular node of the element and interpolate across the element to get average heat flux 

$${\mathbf q_{\textrm{node}} = - k \cdot \nabla T_{\textrm{node}}}$$

here heat flux vector and the temperature gradient are at the node.


3.7. What do you notice when looking at the flux vectors? To be more specific, what does the direction of the vectors tell us? **(1.0 Point)**

Answer: Heat flows in the direction of decreasing temperature T i.e. hot to cold. This is a result of the convention of using a scale that assumes that hotter bodies have a higher temperature than cooler bodies. In this case it point towards the cold region.


3.8. What is the highest temperature? And where does it occur? Is this temperature safe for the structure in terms of material transformations? **(1.5 Points)**

Answer: The highest temperature is 83.52°C or 356.672 K, it occurs at the egde of the hole where it is air-cooled as shown in the image below. It safe to say that the highest temperature won't have significant on the mechanical properties of S235JR [1].

<p align="center">
  <img src="Maxtemperature.png" alt="Highest Temperauture" width="60%">
</p>


3.9. How much heat is transfered due to the water cooling and how much due to the air? How much is this in percentage? **(1.5 Points)**


Answer: The amount of heat flux due to air cooling is:  5.2 W --> 2.5% 

The amount of heat flux due to water cooling is: 194.76 W -->  97.4% 

The sum of heat flux should be 0 but numerically it is 0.034 W. 


### 4. Drilling without water cooling **(3 Points)**

 Hint: if water does not cover the part, something will still cover it.


4.1. Which boundary condition do you need to change? What kind of BC do you set now? **(0.5 Points)**

Answer: We have to change the heatTransferCoefficient = 20 look below for code snippet;
 
<--Heat flux density $\dot{q}_s$ = P/(2*$\pi$*r*h) [W/m^2]-->

heatFlux name="S_hole" value="212206.6"

<--Heat transfer coefficient steel-air 𝛼𝑎𝑖𝑟 in W/(m2·K) & Ambient temperatue of air 𝑇𝑟 in K-->

heatTransport name="S_air" volumeRegion="V_block" heatTransferCoefficient="20" bulkTemperature="293.15"

<--Heat transfer coefficient steel-air 𝛼𝑎𝑖𝑟 in W/(m2·K) & Ambient temperatue of air 𝑇𝑟 in K (without water cooled)-->

heatTransport name="S_cooled" volumeRegion="V_block" heatTransferCoefficient="20" bulkTemperature="293.15"


4.2. Visualize the temperature distribution in paraview (no more than 10 colours) **(1.0 Point)**

<p align="center">
  <img src="temperature_dist_2_step.png" alt="Highest Temperature" width="60%">
</p>

4.3. What is the highest temperature? And where does it occur? Is it safe in terms of material transformations? **(1.0 Point)**

Answer: The highest temperature is 446.15°C or 719.3 K and it occurs at edge of the hole as shown in image with pink dot. With the current temperature it might create some degree of expansion near the hole while drilling [1].  

<p align="center">
  <img src="temperature_dist_2_step.png" alt="Highest Temperature" width="60%">
</p>

4.4. How much heat is now transfered due to the air? How much is this in percentage? **(0.5 Points)**

Answer: The amount of heat flux due to air cooling at the bottom face: 77.102 W --> 38.5% 

The amount of heat flux due to air cooling at side and top faces: 122.9 W --> 61.5% 

### 5. Heat-Mechanic Coupling **(6 Points)**
Determine the effect of the temperature change on the mechanical behaviour of the structure.
Use the case with the water cooling from above.
Assume the structure is free of internal stress in the given initial configuration at a room temperature of 293K.

Generate a suitable simulation input for the coupled simulation to determine the thermal deformations and stresses.


5.1. How shall the (mechanic) boundary condition be chosen in order to fit the description above? **(1.5 Points)**

Answer: We have to assume the structure is free of internal stress in the given initial configuration at a room temperature of 293K i.e., (dof="x", "y", "z" value="0") and clamping for zero displacement (comp dof="x", "y", "z"). Also we need to take into consideration the analysis step 1. i.e. heatConduction PDE since this coupling is modelled as foward coupling from a heat condition simulation.


5.2. Visualize the deformed structure (mind the number of colours) **(1.5 Points)**

<p align="center">
  <img src="deformed.png" alt="Deformed structure" width="60%">
</p>


5.3. What is the maximum deflection, and where does it occur? **(0.5 Points)**

Answer: The maximum deflection is 2.2e-05 m which occurs at lower bottom edge as shown in the image with pink dot.

<p align="center">
  <img src="max_displacement.png" alt="Maximum deflection" width="60%">
</p>


5.4. Visualize the von-Mises stress **(1.0 Point)**

<p align="center">
  <img src="Vonmisses1.png" alt="deferomed structure" width="60%">
</p>

<p align="center">
  <img src="Vonmisses.png" alt="deferomed structure" width="60%">
</p>

5.5. What is the maximum von-Mises stress and where does it occur? Can it be a problem for the structure? **(1.5 Points)**

Answer: The maximum von-Mises stress is 2.5e+08 N/m^2 which occurs at the surface of the hole and is higher than yield strength of 2.25e+08 [1]. This results into plastic deformation of the hole which in-turn leads to reduction in load carring capacity and will fail under cyclic loading.

## Reference
1. https://www.matweb.com/search/datasheet.aspx?matguid=96a3d2463ccb43e3a6c4a48eb0417f13&ckck=1