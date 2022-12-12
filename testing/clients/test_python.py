#!/usr/bin/env python3
import argparse
import umbridge
import pytest

url = "http://model:4242"

def test_supported_models():
  assert umbridge.supported_models(url) == ["forward"]

def test_evaluate():
  model = umbridge.HTTPModel(url, "forward")
  param = [[5e4]*31]
  assert pytest.approx(model(param)[0], 1e-8) == [0.0, 0.0010305185555431918, 0.00398769970980497, 0.00874160408504413, 0.015166746593403382, 0.02314208356583947, 0.032550997847455417, 0.04328128359051827, 0.05522514792620459, 0.06827918055460522, 0.08234433711082555, 0.09732597287604661, 0.11313388801901988, 0.12968239140103968, 0.14689035093904412, 0.16468125026385314, 0.18298325080536978, 0.20172927481502115, 0.22085705474775763, 0.24030915679862971, 0.2600329758429953, 0.27998071014804726, 0.3001093096569888, 0.3203804295432889, 0.3407603753967599, 0.36122006238251075, 0.3817349772122309, 0.40228514200337073, 0.4228550774751416, 0.4434337671927345, 0.4640146361299798]

def test_apply_jacobian():
  model = umbridge.HTTPModel(url, "forward")
  param = [[5e4]*31]
  assert pytest.approx(model.apply_jacobian(0, 0, param, [1.0]*31), 1e-8) == [0.0, -3.0446914977063364e-08, -1.1818488276253744e-07, -2.597003348227248e-07, -4.515692855040442e-07, -6.904588653249138e-07, -9.731271881709425e-07, -1.2964248966599779e-06, -1.657298156286886e-06, -2.0527501178826717e-06, -2.479876654181209e-06, -2.935875245668267e-06, -3.418048457652867e-06, -3.923805485632329e-06, -4.450671427482561e-06, -4.996285738093009e-06, -5.558412274239472e-06, -6.134944703361761e-06, -6.7239034128336145e-06, -7.3234509636131675e-06, -7.931898271703147e-06, -8.547701517420774e-06, -9.169451327842432e-06, -9.795886685089096e-06, -1.0425873291215666e-05, -1.1058422112591528e-05, -1.1692714105741337e-05, -1.2328084763694529e-05, -1.2964030297445511e-05, -1.3600207635953668e-05, -1.4236422063222973e-05]

def test_gradient():
  model = umbridge.HTTPModel(url, "forward")
  param = [[5e4]*31]
  assert pytest.approx(model.gradient(0, 0, param, [1.0]*31), 1e-8) == [-2.932648048015185e-06, -3.942168553400238e-06, -9.922565590361754e-06, -4.978897112303815e-06, 5.280485554023939e-06, 1.2261407080632614e-05, 4.342672272131254e-06, 9.696840162429221e-06, 7.451464965890775e-06, 1.1144695669790261e-05, 1.4793245231223273e-05, 6.004705023140988e-06, 7.3415127709725025e-06, 7.205621299286036e-06, 2.207397762840624e-06, 4.0051161172283134e-07, 6.828119666901777e-06, 2.618658328373824e-07, -7.927133602314562e-06, -4.342845224061809e-06, -1.0238633985776291e-05, -1.2865768823575041e-05, -1.2880966215531031e-05, -2.1388419074036547e-05, -2.907481430093617e-05, -2.6377376498298855e-05, -3.0343264619675514e-05, -3.2412301445225444e-05, -3.1031482808710487e-05, -1.8325226232296377e-05, -1.2232707121556663e-05]

def test_apply_hessian():
  model = umbridge.HTTPModel(url, "forward")
  param = [[5e4]*31]
  assert pytest.approx(model.apply_hessian(0, 0, 0, param, [1.0]*31, [1.0]*31), 1e-8) == [-0.05703084478240826, -0.041081411519430365, -0.03923659546005669, 0.131668368896658, -0.04156037270730176, 0.007001891628034763, -0.029443119033930133, 0.06283699153266527, -0.0036128076986567214, 0.08859551057154422, 0.0530163077335749, -0.08265840765370176, 0.003603003125921904, -0.02572178165599473, 0.020834648088245616, 0.06771274807405922, 0.09832588987597307, -0.02647388952229578, 0.09248623172236516, -0.058374201269659906, 0.07326977781528919, 0.08593666105981546, -0.13732609321979417, 0.028789132595208627, 0.03538424597591204, -0.0031804955508639614, 0.039060820038245944, 0.06574255886703954, 0.09937518031462472, 0.23824901332782716, 0.11510315507144973]

def test_supports():
  model = umbridge.HTTPModel(url, "forward")
  assert model.supports_evaluate()
  assert model.supports_gradient()
  assert model.supports_apply_jacobian()
  assert model.supports_apply_hessian()
