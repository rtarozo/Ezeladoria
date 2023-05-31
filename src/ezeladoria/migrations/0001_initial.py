# Generated by Django 4.2.1 on 2023-05-26 16:17

from django.db import migrations, models
import django.db.models.deletion
import localflavor.br.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('Banco_Id', models.AutoField(primary_key=True, serialize=False, verbose_name='Sequencia')),
                ('Banco_Codigo', models.CharField(help_text='Código', max_length=4)),
                ('Descricao', models.CharField(help_text='Descrição', max_length=50)),
                ('Inativo', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Banco',
                'verbose_name_plural': 'Bancos',
            },
        ),
        migrations.CreateModel(
            name='ContaCorrente',
            fields=[
                ('Conta_Corrente_Id', models.AutoField(primary_key=True, serialize=False, verbose_name='Código Conta')),
                ('Tipo_Conta', models.CharField(choices=[('11', 'Física'), ('12', 'Jurídica'), ('13', 'Poupança'), ('14', 'Aplicação'), ('15', 'Juros'), ('16', 'Multa')], max_length=2)),
                ('Codigo_Conta', models.IntegerField(default=0, verbose_name='Número Conta')),
                ('Digito_Conta', models.IntegerField(default=0, verbose_name='Dv')),
                ('Descricao', models.CharField(help_text='Descrição', max_length=50, verbose_name='Descrição')),
                ('Data_Cadastro', models.DateField(auto_now_add=True, db_index=True, verbose_name='Data de Cadastro')),
                ('Saldo', models.FloatField(blank=True, default=0.0, null=True)),
                ('Data_Atualizacao', models.DateField(auto_now=True, db_index=True, verbose_name='Data de Atualização')),
                ('Limite_Credito', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Limite de Crédito')),
            ],
            options={
                'verbose_name': 'Conta Corrente',
                'verbose_name_plural': 'Contas\xa0Corrente',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('Empresa_Id', models.AutoField(primary_key=True, serialize=False, verbose_name='Código Empresa')),
                ('Razao_Social', models.CharField(help_text='Razão Social da empresa', max_length=100)),
                ('Nome_Fantasia', models.CharField(help_text='Nome Fantasia da empresa', max_length=50)),
                ('CNPJ', localflavor.br.models.BRCNPJField(help_text='CNPJ da empresa', max_length=18, verbose_name='CNPJ da empresa')),
                ('Email_Principal', models.EmailField(help_text='Email do responsável', max_length=100, verbose_name='Email')),
                ('Data_Cadastro', models.DateField(auto_now_add=True, db_index=True, verbose_name='Data de Cadastro')),
                ('Inativo', models.BooleanField(default=False, verbose_name='Inativo')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Logradouro', models.CharField(max_length=100)),
                ('Numero', models.CharField(blank=True, max_length=15, null=True)),
                ('Complemento', models.CharField(blank=True, max_length=40, null=True)),
                ('Estado', localflavor.br.models.BRStateField(default='SP', max_length=2)),
                ('Bairro', models.CharField(max_length=50)),
                ('Cidade', models.CharField(max_length=100)),
                ('Pais', models.CharField(max_length=50)),
                ('CEP', localflavor.br.models.BRPostalCodeField(max_length=9)),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
        migrations.CreateModel(
            name='HistoricoPadrao',
            fields=[
                ('Historico_Id', models.AutoField(primary_key=True, serialize=False, verbose_name='Código Histórico')),
                ('Descricao', models.CharField(help_text='Descrição', max_length=50)),
                ('Historico', models.TextField(help_text='Histórico', max_length=200)),
                ('Inativo', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Histórico Padrão',
                'verbose_name_plural': 'Históricos Padrões',
            },
        ),
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('Parametro_Id', models.AutoField(primary_key=True, serialize=False, verbose_name='Sequencia Parametro')),
                ('Descricao', models.CharField(help_text='Descrição', max_length=50)),
                ('Codigo', models.CharField(help_text='Código', max_length=50)),
                ('Valor', models.TextField(help_text='Valor', max_length=200)),
            ],
            options={
                'verbose_name': 'Parametro',
                'verbose_name_plural': 'Parametros',
            },
        ),
        migrations.CreateModel(
            name='TipoEvento',
            fields=[
                ('Tipo_Evento_Id', models.AutoField(primary_key=True, serialize=False, verbose_name='Código Tipo')),
                ('Descricao', models.CharField(help_text='Descrição', max_length=50, verbose_name='Descrição')),
                ('Inativo', models.BooleanField(default=False, verbose_name='Inativo')),
            ],
            options={
                'verbose_name': 'Tipo de Evento',
                'verbose_name_plural': 'Tipos de Eventos',
            },
        ),
        migrations.CreateModel(
            name='Orgao_Responsavel',
            fields=[
                ('Acionaveis_Id', models.AutoField(primary_key=True, serialize=False, verbose_name='Sequencia')),
                ('Descricao', models.CharField(help_text='Descrição', max_length=50, verbose_name='Descrição')),
                ('Inativo', models.BooleanField(default=False, verbose_name='Inativo')),
                ('Email_Principal', models.EmailField(help_text='Email do responsável', max_length=100, verbose_name='Email')),
                ('Data_Cadastro', models.DateField(auto_now_add=True, verbose_name='Data de Cadastro')),
                ('Empresa', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='Orgao_Responsavel.Empresa+', to='ezeladoria.empresa')),
                ('Tipo_Evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ezeladoria.tipoevento')),
            ],
            options={
                'verbose_name': 'Orgão Responsável',
                'verbose_name_plural': 'Orgãos Responsáveis',
            },
        ),
        migrations.CreateModel(
            name='LancamentoConta',
            fields=[
                ('Lancamento_Id', models.AutoField(primary_key=True, serialize=False, verbose_name='Código Lançamento')),
                ('Data_lancamento', models.DateField(auto_now_add=True, db_index=True, verbose_name='Data de Lançamento')),
                ('Tipo_Lacamento', models.CharField(choices=[('D', 'Débito'), ('C', 'Crédito')], max_length=1)),
                ('Saldo_Anterior', models.FloatField(default=0.0)),
                ('Valor_Debito', models.FloatField(default=0.0)),
                ('Valor_Credito', models.FloatField(default=0.0)),
                ('Saldo_Atual', models.FloatField(default=0.0)),
                ('Historico_Lancamento', models.TextField(help_text='Histórico', max_length=200)),
                ('ContaCorrente_Id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ContaCorrente', to='ezeladoria.contacorrente')),
                ('Historico_Id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Históricos', to='ezeladoria.historicopadrao')),
            ],
            options={
                'verbose_name': 'Lançamento em Conta',
                'verbose_name_plural': 'Lançamentos em Conta',
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('Evento_Id', models.AutoField(primary_key=True, serialize=False, verbose_name='Sequencia')),
                ('Data_Cadastro', models.DateField(auto_now_add=True, db_index=True, verbose_name='Data de Cadastro')),
                ('Longitude', models.FloatField(default=0.0)),
                ('Latitude', models.FloatField(default=0.0)),
                ('Foto', models.ImageField(upload_to='medias/')),
                ('Status', models.CharField(choices=[('0', 'Enviado'), ('1', 'Recebido'), ('2', 'Em Analise'), ('3', 'Encaminhado'), ('4', 'Aguardando Solução'), ('5', 'Cancelado'), ('6', 'Resolvido')], max_length=2)),
                ('Empresa', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='ezeladoria.Evento.Empresa+', to='ezeladoria.empresa')),
                ('Endrereco', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ezeladoria.endereco')),
                ('Tipo_Evento_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ezeladoria.tipoevento')),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
        migrations.AddField(
            model_name='empresa',
            name='Endereco',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ezeladoria.endereco'),
        ),
        migrations.AddField(
            model_name='contacorrente',
            name='Empresa',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='Empresa', to='ezeladoria.empresa'),
        ),
        migrations.CreateModel(
            name='ContaBanco',
            fields=[
                ('Conta_Corrente_Id', models.AutoField(primary_key=True, serialize=False, verbose_name='Sequencia')),
                ('Codigo_Conta', models.IntegerField(default=0, unique=True, verbose_name='Número Conta')),
                ('Digito_Conta', models.IntegerField(default=0, verbose_name='Dv')),
                ('Agencia', models.CharField(default=0, help_text='Agência e DV', max_length=6, verbose_name='Agência e DV')),
                ('Descricao', models.CharField(help_text='Descrição', max_length=50, verbose_name='Descrição')),
                ('Data_Cadastro', models.DateField(auto_now_add=True, db_index=True, verbose_name='Data de Cadastro')),
                ('Saldo', models.FloatField(blank=True, default=0.0, null=True)),
                ('Data_Atualizacao', models.DateField(auto_now=True, db_index=True, verbose_name='Data de Atualização')),
                ('Limite_Credito', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Limite de Crédito')),
                ('Inativo', models.BooleanField(default=False)),
                ('Banco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Banco', to='ezeladoria.banco')),
            ],
            options={
                'verbose_name': 'Conta',
                'verbose_name_plural': 'Contas',
            },
        ),
    ]